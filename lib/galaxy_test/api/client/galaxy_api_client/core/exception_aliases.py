from httpx import Response

from galaxy_test.api.client.galaxy_api_client.core.exceptions import ClientError, ServerError


class Error200(ClientError):
    """Exception alias for HTTP 200 responses."""

    def __init__(self, response: Response) -> None:
        super().__init__(status_code=response.status_code, message=response.text, response=response)


class Error202(ClientError):
    """Exception alias for HTTP 202 responses."""

    def __init__(self, response: Response) -> None:
        super().__init__(status_code=response.status_code, message=response.text, response=response)


class Error204(ClientError):
    """Exception alias for HTTP 204 responses."""

    def __init__(self, response: Response) -> None:
        super().__init__(status_code=response.status_code, message=response.text, response=response)


class Error304(ClientError):
    """Exception alias for HTTP 304 responses."""

    def __init__(self, response: Response) -> None:
        super().__init__(status_code=response.status_code, message=response.text, response=response)


class Error404(ClientError):
    """Exception alias for HTTP 404 responses."""

    def __init__(self, response: Response) -> None:
        super().__init__(status_code=response.status_code, message=response.text, response=response)


class Error501(ServerError):
    """Exception alias for HTTP 501 responses."""

    def __init__(self, response: Response) -> None:
        super().__init__(status_code=response.status_code, message=response.text, response=response)


__all__ = ["Error200", "Error202", "Error204", "Error304", "Error404", "Error501"]
