from apistar.renderers import HTMLRenderer, JSONRenderer
from common.auth.auth import SessionAuthentication, TokenAuthentication, BasicAuthentication
from apistar.hooks import render_response
from common.hooks import handle_options


settings = {
    "MONGO": {
        "host": "localhost",
    },
    "AUTHENTICATION": [
        SessionAuthentication(),
        TokenAuthentication(),
        BasicAuthentication(),
    ],
    'STATICS': {
        'ROOT_DIR': 'web/dist',       # Include the 'statics/' directory.
        'PACKAGE_DIRS': ['apistar']  # Include the built-in apistar static files.
    },
    "AFTER_REQUEST": [
        render_response,
        handle_options
        # AcceptOrigin,
    ],
    'RENDERERS': [JSONRenderer(), HTMLRenderer()]
}