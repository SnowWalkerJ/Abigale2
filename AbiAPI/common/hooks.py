import os
from apistar import Settings, exceptions, http
from apistar.interfaces import Injector
from apistar.renderers import DEFAULT_RENDERERS, negotiate_renderer
from apistar.types import Handler, ReturnValue


def AcceptOrigin(method: http.Method, response: ReturnValue):
    response.headers["Access-Control-Allow-Origin"]      = os.environ.get("ABI_ALLOW_ORIGIN", "*")
    response.headers["Access-Control-Allow-Methods"]     = "GET,POST,PUT,DELETE,OPTIONS,HEADERS"
    response.headers["Access-Control-Allow-Headers"]     = "Authorization,Content-Type,X-Requested-With"
    response.headers["Access-Control-Expose-Headers"]    = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response


def handle_options(method: http.Method, response: ReturnValue):
    if method.lower() == "options":
        response.status = 200
        response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS,HEADERS"
        response.headers["Allow"] = "GET,POST,PUT,DELETE,OPTIONS,HEADERS"
        response.headers["Access-Control-Allow-Headers"] = "Authorization,Content-Type,X-Requested-With"
    return response
