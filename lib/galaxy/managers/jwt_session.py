"""JWT-based session management for Galaxy.

Replaces database-backed galaxy_session rows with signed JWTs for:
- Authenticated users: short-lived access JWT + DB-backed refresh token
- Anonymous users: signed JWT with optional history_id/session_id (lazy DB session)
"""

import hashlib
import hmac
import logging
import secrets
from datetime import (
    datetime,
    timedelta,
    timezone,
)
from typing import Optional

import jwt
from sqlalchemy import (
    select,
    true,
)

from galaxy.model import SessionRefreshToken
from galaxy.model.base import transaction

log = logging.getLogger(__name__)

# JWT claim type values
TOKEN_TYPE_SESSION = "session"
TOKEN_TYPE_ANONYMOUS = "anon"


class JWTSessionManager:
    """Manages JWT-based session tokens and refresh tokens."""

    def __init__(
        self,
        secret: str,
        access_ttl: int = 900,
        refresh_ttl: int = 2592000,
    ):
        """
        :param secret: Signing key for JWTs (derived from id_secret or explicit config).
        :param access_ttl: Access token lifetime in seconds (default 15 minutes).
        :param refresh_ttl: Refresh token lifetime in seconds (default 30 days).
        """
        self.secret = secret
        self.access_ttl = access_ttl
        self.refresh_ttl = refresh_ttl
        self.algorithm = "HS256"

    @staticmethod
    def derive_secret(id_secret: str) -> str:
        """Derive a JWT signing key from Galaxy's id_secret."""
        return hmac.new(
            id_secret.encode("utf-8"),
            b"galaxy-session-jwt",
            hashlib.sha256,
        ).hexdigest()

    # --- Authenticated user tokens ---

    def create_access_token(self, user_id: int) -> str:
        """Create a short-lived access JWT for an authenticated user."""
        now = datetime.now(timezone.utc)
        payload = {
            "type": TOKEN_TYPE_SESSION,
            "sub": str(user_id),
            "iat": now,
            "exp": now + _timedelta_seconds(self.access_ttl),
        }
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)

    def create_refresh_token(self, user_id: int, sa_session) -> str:
        """Create a refresh token, store its SHA-256 hash in the DB, return the raw token."""
        raw_token = secrets.token_urlsafe(48)
        token_hash = hashlib.sha256(raw_token.encode("utf-8")).hexdigest()
        now = datetime.now(timezone.utc)
        refresh = SessionRefreshToken(
            user_id=user_id,
            token_hash=token_hash,
            created_at=now,
            expires_at=now + _timedelta_seconds(self.refresh_ttl),
            is_valid=True,
        )
        sa_session.add(refresh)
        with transaction(sa_session):
            sa_session.commit()
        return raw_token

    def verify_refresh_token(self, raw_token: str, sa_session) -> Optional[SessionRefreshToken]:
        """Verify a refresh token against the DB. Returns the DB row if valid, else None."""
        token_hash = hashlib.sha256(raw_token.encode("utf-8")).hexdigest()
        now = datetime.now(timezone.utc)
        stmt = (
            select(SessionRefreshToken)
            .where(SessionRefreshToken.token_hash == token_hash)
            .where(SessionRefreshToken.is_valid == true())
            .where(SessionRefreshToken.expires_at > now)
            .limit(1)
        )
        return sa_session.scalars(stmt).first()

    def revoke_refresh_token(self, raw_token: str, sa_session) -> None:
        """Revoke a single refresh token (per-session logout)."""
        token_hash = hashlib.sha256(raw_token.encode("utf-8")).hexdigest()
        stmt = (
            select(SessionRefreshToken)
            .where(SessionRefreshToken.token_hash == token_hash)
            .limit(1)
        )
        refresh = sa_session.scalars(stmt).first()
        if refresh:
            refresh.is_valid = False
            sa_session.add(refresh)
            with transaction(sa_session):
                sa_session.commit()

    def revoke_all_refresh_tokens(self, user_id: int, sa_session) -> None:
        """Revoke all refresh tokens for a user (logout all sessions)."""
        stmt = (
            select(SessionRefreshToken)
            .where(SessionRefreshToken.user_id == user_id)
            .where(SessionRefreshToken.is_valid == true())
        )
        for refresh in sa_session.scalars(stmt):
            refresh.is_valid = False
            sa_session.add(refresh)
        with transaction(sa_session):
            sa_session.commit()

    # --- Anonymous tokens ---

    def create_anonymous_token(
        self,
        history_id: Optional[int] = None,
        session_id: Optional[int] = None,
    ) -> str:
        """Create a signed JWT for an anonymous user.

        If the anonymous user has created a history, history_id and session_id
        reference the lazily-created DB records.
        """
        now = datetime.now(timezone.utc)
        payload: dict = {
            "type": TOKEN_TYPE_ANONYMOUS,
            "iat": now,
            "exp": now + _timedelta_seconds(self.refresh_ttl),  # Same TTL as refresh (90 days)
        }
        if history_id is not None:
            payload["history_id"] = history_id
        if session_id is not None:
            payload["session_id"] = session_id
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)

    # --- Generic decode ---

    def decode_token(self, token: str) -> Optional[dict]:
        """Decode and verify a JWT. Returns claims dict or None if invalid/expired."""
        try:
            return jwt.decode(token, self.secret, algorithms=[self.algorithm])
        except jwt.ExpiredSignatureError:
            log.debug("JWT expired")
            return None
        except jwt.InvalidTokenError as e:
            log.debug("Invalid JWT: %s", e)
            return None

    def is_jwt(self, cookie_value: str) -> bool:
        """Check if a cookie value is a JWT (contains dots) vs legacy Blowfish-encrypted session key."""
        return "." in cookie_value


def _timedelta_seconds(seconds: int):
    """Create a timedelta from seconds."""
    return timedelta(seconds=seconds)
