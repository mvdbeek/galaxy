"""
Galaxy web application framework
"""

from urllib.parse import urlencode

from starlette.routing import (
    BaseRoute,
    NoMatchFound,
)

from . import base

DEPRECATED_URL_ATTRIBUTE_MESSAGE = "*deprecated attribute, URL not filled in by server*"


class UrlFor:
    """Resolve a URL by name, trying FastAPI routes first then WSGI routes.

    The ``route_name_index`` is set once at startup by ``initialize_fast_app``
    and is immutable after that.
    """

    route_name_index: dict[str, list[BaseRoute]]

    def __init__(self):
        self.route_name_index = {}

    def __call__(self, *args, **kwargs) -> str:
        qualified = kwargs.pop("qualified", False)
        query_params = kwargs.pop("query_params", None)

        # Try FastAPI route index first
        if self.route_name_index and args:
            name = args[0]
            candidates = self.route_name_index.get(name)
            if candidates is not None:
                for route in candidates:
                    try:
                        url = str(route.url_path_for(name, **kwargs))
                        if query_params:
                            url = f"{url}?{urlencode(query_params)}"
                        return url
                    except (NoMatchFound, TypeError):
                        pass

        # Fall back to WSGI routes.url_for
        try:
            if query_params:
                kwargs.update(query_params)
            if qualified:
                kwargs["qualified"] = qualified
            return base.routes.url_for(*args, **kwargs)
        except AttributeError:
            return DEPRECATED_URL_ATTRIBUTE_MESSAGE


url_for = UrlFor()
