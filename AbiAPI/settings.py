import os
from apistar.renderers import HTMLRenderer, JSONRenderer
from common.auth.auth import SessionAuthentication, TokenAuthentication, BasicAuthentication
from apistar.hooks import render_response
from common.hooks import handle_options, AcceptOrigin


settings = {
    "MONGO": {
        "host": os.environ.get("ABI_MONGO_HOST", "localhost"),
        "user": os.environ.get("ABI_MONGO_USER", "abigale"),
        "password": os.environ.get("ABI_MONGO_PASSWORD", "abigale"),
    },
    "AUTHENTICATION": [
        SessionAuthentication(),
        TokenAuthentication(),
        BasicAuthentication(),
    ],
    'STATICS': {
        'ROOT_DIR': 'web/dist',       # Include the 'statics/' directory.
        'PACKAGE_DIRS': ['apistar']   # Include the built-in apistar static files.
    },
    "AFTER_REQUEST": [
        render_response,
        handle_options,
        AcceptOrigin,
    ],
    'RENDERERS': [JSONRenderer(), HTMLRenderer()]
}
