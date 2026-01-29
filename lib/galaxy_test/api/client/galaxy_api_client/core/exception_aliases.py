from httpx import Response

from galaxy_test.api.client.galaxy_api_client.core.exceptions import ClientError, ServerError


class NotFoundError(ClientError):
    """HTTP 404 Not Found.

    Raised when the server responds with a 404 status code."""

    def __init__(self, response: Response) -> None:
        """Initialise NotFoundError with the HTTP response.

        Args:
            response: The httpx Response object that triggered this exception
        """
        super().__init__(status_code=response.status_code, message=response.text, response=response)


class HttpNotImplementedError(ServerError):
    """HTTP 501 Not Implemented.

    Raised when the server responds with a 501 status code."""

    def __init__(self, response: Response) -> None:
        """Initialise HttpNotImplementedError with the HTTP response.

        Args:
            response: The httpx Response object that triggered this exception
        """
        super().__init__(status_code=response.status_code, message=response.text, response=response)


__all__ = ["HttpNotImplementedError", "NotFoundError"]
