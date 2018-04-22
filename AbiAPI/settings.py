from apistar import hooks
# from auth import BasicAuthentication, TokenAuthentication
from common.misc import AcceptOrigin


settings = {
    "MONGO": {
        "host": "192.168.0.105",
    },
    # "AUTHENTICATION": [
    #     BasicAuthentication(),
    #     TokenAuthentication(),
    # ],
    'STATICS': {
        'ROOT_DIR': 'dist',       # Include the 'statics/' directory.
        'PACKAGE_DIRS': ['apistar']  # Include the built-in apistar static files.
    },
    "AFTER_REQUEST": [
        hooks.render_response,
        AcceptOrigin,
    ]
}