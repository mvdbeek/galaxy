"""
Base client with shared functionality for sync and async clients.
"""

from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)
R = TypeVar("R")


@dataclass
class Response(Generic[T]):
    """Wrapper for API responses with metadata."""

    data: T
    status_code: int
    headers: dict[str, str]
    response_time: float


@dataclass
class File:
    """Represents a file to be uploaded."""

    content: bytes
    filename: str
    content_type: str | None = None

    def to_tuple(self) -> tuple[str, bytes] | tuple[str, bytes, str]:
        """Convert to tuple format expected by httpx."""
        if self.content_type:
            return (self.filename, self.content, self.content_type)
        return (self.filename, self.content)


class ApiError(Exception):
    """Base exception for API errors."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        response_body: Any | None = None,
    ):
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body


class ValidationError(ApiError):
    """Raised when request validation fails."""

    pass


class AuthenticationError(ApiError):
    """Raised when authentication fails."""

    pass


class NotFoundError(ApiError):
    """Raised when resource is not found."""

    pass


class BaseClient:
    """
    Base client with shared configuration.
    """

    def __init__(
        self,
        base_url: str,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        timeout: float = 30.0,
        verify_ssl: bool = True,
        follow_redirects: bool = True,
        default_headers: dict[str, str] | None = None,
    ):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.bearer_token = bearer_token
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.follow_redirects = follow_redirects
        self.default_headers = default_headers or {}

    def _get_headers(self) -> dict[str, str]:
        """Construct headers with authentication."""
        headers = self.default_headers.copy()

        if self.api_key:
            headers["X-API-Key"] = self.api_key
        elif self.bearer_token:
            headers["Authorization"] = f"Bearer {self.bearer_token}"

        return headers

    def _filter_none_values(self, params: dict[str, Any]) -> dict[str, Any]:
        """Filter out None values from parameters to avoid sending them as 'None' strings."""
        return {k: v for k, v in params.items() if v is not None}

    def _handle_response(self, response) -> Any:
        """Handle API response and errors."""
        if response.status_code == 401:
            raise AuthenticationError("Authentication failed", status_code=401)
        elif response.status_code == 404:
            raise NotFoundError("Resource not found", status_code=404)
        elif response.status_code >= 400:
            raise ApiError(
                f"API error: {response.text}",
                status_code=response.status_code,
                response_body=response.text,
            )

        return response

    def _handle_streaming_response(self, response) -> Any:
        """Handle streaming response and errors (doesn't access .text property)."""
        if response.status_code == 401:
            raise AuthenticationError("Authentication failed", status_code=401)
        elif response.status_code == 404:
            raise NotFoundError("Resource not found", status_code=404)
        elif response.status_code >= 400:
            raise ApiError(
                f"API error (status: {response.status_code})",
                status_code=response.status_code,
                response_body="",
            )

        return response
