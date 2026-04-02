# JWT Session Management for Galaxy

## Problem Statement

Galaxy's `galaxy_session` table has 200 million rows, of which **196 million are anonymous**
(`user_id IS NULL`). Every web request from a non-logged-in user (including bots and crawlers)
creates a DB row. Most anonymous sessions never get a history — histories are lazy-created only
when the UI client requests one. The table is essentially a graveyard of one-time anonymous
session rows that causes performance issues and requires regular manual cleanup via
`delete_galaxy_sessions.py`.

### Key data points

```sql
-- 98% of sessions are anonymous
SELECT count(*) FROM galaxy_session WHERE user_id IS NULL;  -- 196,466,821
SELECT count(*) FROM galaxy_session;                         -- ~200,000,000
```

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Anonymous without history | JWT cookie only, **no DB row** | Bots, crawlers, casual visitors create zero DB rows |
| Anonymous with history | **Lazy DB session** — created when history is created | Jobs FK to `galaxy_session.id` for `remote_host`/`remote_addr` tracing; audit logs also reference sessions |
| Authenticated users | **Short-lived access JWT** (15 min) + **refresh token** in DB | Stateless per-request verification; DB lookup only on refresh (~every 15 min) |
| Multi-session support | Yes — each login creates a separate refresh token row | Users can be logged in from multiple browsers/devices simultaneously |
| Per-session logout | Revoke that session's refresh token; access JWT expires in ≤15 min | Precise control without invalidating other sessions |
| Logout all | Revoke all refresh tokens for the user | Covers password change, account compromise scenarios |
| Migration | Cookie format detection (JWT has dots, legacy Blowfish-encrypted hex doesn't) — both work simultaneously | Zero-downtime rollout, easy rollback via `use_jwt_sessions=false` |
| Session disk_usage | Not used (dead code) | Only `User.disk_usage` is actively used; `GalaxySession.disk_usage` is never written to |

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Request arrives                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Cookie contains "." ?  ──yes──► JWT path                       │
│         │                        │                              │
│         no                       ├─ type=session (authenticated) │
│         │                        │   → verify JWT (stateless)   │
│         ▼                        │   → if expired, try refresh  │
│  Legacy DB session               │   → load User, no DB session │
│  lookup (unchanged)              │                              │
│                                  ├─ type=anon + session_id      │
│                                  │   → load DB session (has     │
│                                  │     history)                 │
│                                  │                              │
│                                  ├─ type=anon (no session_id)   │
│                                  │   → JWTSessionAdapter()      │
│                                  │   → NO DB row                │
│                                  │                              │
│  No cookie at all ───────────────┤                              │
│                                  └─ Issue anonymous JWT         │
│                                     → NO DB row                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│              Anonymous user creates history                     │
├─────────────────────────────────────────────────────────────────┤
│  1. Create GalaxySession DB row (user_id=NULL,                  │
│     remote_host, remote_addr from request)                      │
│  2. Create History (user=None)                                  │
│  3. Create GalaxySessionToHistoryAssociation                    │
│  4. Reissue JWT: {type:anon, history_id:X, session_id:Y}       │
│  5. job.session_id → remote_addr tracing preserved              │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│              Login flow (anonymous → authenticated)              │
├─────────────────────────────────────────────────────────────────┤
│  1. Extract history_id from anonymous JWT (if any)              │
│  2. Invalidate anonymous DB session (if exists)                 │
│  3. Transfer anonymous history to user                          │
│  4. Create refresh token → store hash in session_refresh_token  │
│  5. Issue access JWT: {type:session, sub:user_id}               │
│  6. Set galaxysession + galaxysession_refresh cookies           │
└─────────────────────────────────────────────────────────────────┘
```

## Impact

| Scenario | DB rows before | DB rows after |
|----------|---------------|---------------|
| Bot/crawler visit | 1 `galaxy_session` INSERT | **0** |
| Anonymous visitor (no history) | 1 `galaxy_session` INSERT | **0** |
| Anonymous user creates history | 1 `galaxy_session` (already existed) | 1 `galaxy_session` (lazy) |
| Authenticated login | 1 `galaxy_session` INSERT | 1 `session_refresh_token` INSERT |
| Per-request DB cost (authenticated) | 1 SELECT on `galaxy_session` | **0** (JWT stateless; refresh only every 15 min) |

**Expected reduction: ~190M+ fewer `galaxy_session` rows** (bots, crawlers, visitors without histories).

## Configuration

```yaml
# galaxy.yml
use_jwt_sessions: false          # Feature flag (default: disabled)
session_jwt_secret: null          # Derived from id_secret if not set
jwt_access_token_ttl: 900         # 15 minutes
jwt_refresh_token_ttl: 2592000    # 30 days
```

## Files Modified

| File | Change |
|------|--------|
| `lib/galaxy/managers/jwt_session.py` | **NEW** — `JWTSessionManager` with HS256 JWT + refresh token CRUD |
| `lib/galaxy/model/__init__.py` | `SessionRefreshToken` model + `JWTSessionAdapter` class |
| `lib/galaxy/model/migrations/alembic/versions_gxy/5ad6cbdbb7b8_...` | **NEW** — `session_refresh_token` table |
| `lib/galaxy/webapps/base/webapp.py` | `_ensure_valid_session` (JWT path), `handle_user_login/logout` (JWT flows), `new_history` (lazy DB session), `set_history`, `set_user` |
| `lib/galaxy/webapps/galaxy/api/__init__.py` | `get_session()` JWT cookie support |
| `lib/galaxy/config/schemas/config_schema.yml` | 4 new config options |
| `lib/galaxy/model/scripts/delete_galaxy_sessions.py` | Also cleans expired refresh tokens |

## Key Technical Details

### Cookie Format Detection
- Legacy: Blowfish-encrypted hex string (no dots) — e.g. `a1b2c3d4e5f6...`
- JWT: `header.payload.signature` format (contains dots) — e.g. `eyJhbGci...`
- Detection: `"." in cookie_value`

### JWT Signing Key
- Derived from `id_secret`: `HMAC-SHA256(id_secret, b"galaxy-session-jwt")`
- Or explicit `session_jwt_secret` config
- Algorithm: HS256 via PyJWT (already a Galaxy dependency)

### Refresh Token Storage
- Raw token: `secrets.token_urlsafe(48)` — given to client in cookie
- Stored as: `SHA-256(raw_token)` in `session_refresh_token.token_hash`
- Never stored in plaintext

### JWTSessionAdapter
Duck-types as `GalaxySession` so all downstream code (`trans.galaxy_session.user`,
`.current_history`, `.id`, `.remote_addr`) works unchanged. Wraps a lazily-created
`GalaxySession` DB row via `_db_session` attribute when anonymous users create histories.

## Testing Requirements

1. **Unit tests**: JWT create/verify/expire, refresh token CRUD, anonymous tokens
2. **Unit tests**: `JWTSessionAdapter` interface compatibility with `GalaxySession`
3. **Integration tests**:
   - Anonymous visit → no `galaxy_session` row, JWT cookie set
   - Anonymous creates history → `galaxy_session` row created lazily, JWT updated
   - Anonymous runs job → `job.session_id` valid, `remote_addr` traceable
   - Anonymous → login → history transferred, access JWT + refresh cookie issued
   - Authenticated request with valid access JWT → no session DB query
   - Access JWT expired + valid refresh → new access JWT issued transparently
   - Access JWT expired + revoked refresh → treated as new anonymous
   - Logout → that refresh token revoked, other sessions unaffected
   - Logout all → all refresh tokens revoked
   - Legacy cookie → still works during migration
4. **Selenium**: `test_anon_history.py` passes unchanged
5. **Rollback**: `use_jwt_sessions=false` → reverts to DB sessions
