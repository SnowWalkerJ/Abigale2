from apistar import hooks
from apistar.renderers import HTMLRenderer, JSONRenderer
from common.auth.auth import SessionAuthentication, TokenAuthentication, BasicAuthentication
from common.misc import AcceptOrigin


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
        hooks.render_response,
        # AcceptOrigin,
    ],
    'RENDERERS': [HTMLRenderer(), JSONRenderer()]
}