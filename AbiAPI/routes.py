from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls, serve_static
from apps.details import detail_routes
from apps.files import file_routes
from apps.users import user_routes
from apps.login import login, logout
from apps.index import index


api_routes = [
    Include('/details', detail_routes),
    Include('/files', file_routes),
    Include('/users', user_routes),
    Route('/login', 'POST', login),
    Route('/logout', 'GET', logout),
]

routes = [
    Include('/api', api_routes),
    Include('/docs', docs_urls),
    Route('/dist/{path}', 'GET', serve_static),
    Route('/', 'GET', index),
    # Include('/static', static_urls)
]


for path in ('/details', '/login', '/fileList', '/admin'):
    routes.append(Route(path, 'GET', index, name=path))
