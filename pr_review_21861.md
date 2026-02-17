## Concern: Existing accounts with mixed-case emails

This PR correctly identifies and fixes the entry points where emails can slip into the database without normalization. However, I'm concerned about the **transition path for existing accounts** that already have mixed-case emails stored.

### No data migration for existing emails

After this PR lands, new accounts will always have lowercase emails, but existing accounts (e.g. `User@Example.com`) remain as-is. This creates a split world that can cause several concrete problems:

### 1. Duplicate account creation

`_error_on_duplicate_email()` calls `get_user_by_email()` which is **case-sensitive by default** (`lib/galaxy/model/db/user.py:27`). If `User@Example.com` exists in the database and someone registers `user@example.com`, the duplicate check passes (different case), and depending on the database collation (PostgreSQL default is case-sensitive), a second account could be created for the same logical email address.

### 2. Remote user session invalidation

In `lib/galaxy/webapps/base/webapp.py:629`:
```python
galaxy_session.user.email != remote_user_email
```
After this PR, `remote_user_email` is lowercased, but the stored email for an existing user may still be `User@Example.com`. This mismatch would **invalidate the session on every request** and trigger `get_or_create_remote_user()`, which would attempt to create a new user with the lowercased email — potentially creating a duplicate or failing on the unique constraint.

### 3. `by_email()` is strictly case-sensitive

`get_user_by_identity()` and `get_reset_token()` both fall back to `_get_user_by_email_case_insensitive()`, so login and password reset work. But `by_email()` at `lib/galaxy/managers/users.py:284` has **no such fallback** and would fail to find existing mixed-case accounts when queried with a lowercased email.

### Suggestions

1. **Add an Alembic data migration** to lowercase all existing emails. This needs to detect and handle case-insensitive duplicates (e.g. both `User@Example.com` and `user@example.com` exist) — possibly by merging or flagging for admin review. The existing `EmailDeduplicator` in `lib/galaxy/model/migrations/data_fixes/user_table_fixer.py` does case-*sensitive* deduplication and could serve as a starting point.

2. **Make the duplicate check case-insensitive** — `_error_on_duplicate_email()` should use a case-insensitive lookup so that registering `user@example.com` is blocked when `User@Example.com` already exists.

3. **Fix the remote user session comparison** in `webapp.py:629` to be case-insensitive, or normalize the stored email before comparing, to avoid session churn for existing accounts.

4. **Consider a case-insensitive unique index** on the email column (e.g. `CREATE UNIQUE INDEX ON galaxy_user (lower(email))`) to provide a database-level guarantee rather than relying solely on application-level lowercasing at every entry point.
