import uvicorn
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.routing import GraphQlSubscriptionRoute
from starlette.graphql import GraphQLApp


from galaxy_main import (
    GalaxyConfigBuilder,
    main,
)

from galaxy.util.properties import load_app_properties
from galaxy.webapps.galaxy.buildapp import app_factory


def wsgiloop(args, log):
    # TODO: How can we build the configuration when starting uvicorn/gunicorn externally with unicorn fapi.py:app ?
    config_builder = GalaxyConfigBuilder(args)
    kwds = config_builder.app_kwds()
    kwds = load_app_properties(**kwds)
    gx = app_factory(global_conf=config_builder.global_conf(), **kwds)
    wsgi_handler = WSGIMiddleware(gx)

    # app factory will import api controllers while passing in app object,
    # this needs to happen before we can import the router from individual api modules
    # (until we've replaced everything with FastAPI, at which point we can do normal imports).
    from galaxy.webapps.galaxy.api import jobs
    from galaxy.webapps.galaxy.api import websocket
    from galaxy.webapps.galaxy.api import graphql
    subscription_routes = [GraphQlSubscriptionRoute("/subscriptions", schema=graphql.schema)]
    # Seems like maybe a bug in FastAPI, but passing in the router in the main app was the only way
    # in which I could get the GraphQlSubscriptionRoute to work.
    # Would be nicer to just include a router.
    app = FastAPI(routes=subscription_routes)
    app.include_router(websocket.router, prefix='/api/websocket')
    app.include_router(jobs.router, prefix='/api/jobs')
    app.add_route('/graphql', GraphQLApp(schema=graphql.schema))
    app.mount('/', wsgi_handler)
    uvicorn.run(app)


if __name__ == '__main__':
    main(wsgiloop)
