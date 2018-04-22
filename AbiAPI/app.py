from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls, serve_static
from apps.details import detail_routes
from commands import commands
from components import components
from settings import settings


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


api_routes = [
    Include('/details', detail_routes),
]


routes = [
    Route('/', 'GET', welcome),
    Include('/api', api_routes),
    Include('/docs', docs_urls),
    Route('/dist/{path}', 'GET', serve_static)
    # Include('/static', static_urls)
]

app = App(
    routes=routes,
    components=components,
    commands=commands,
    settings=settings
)


if __name__ == '__main__':
    app.main()
