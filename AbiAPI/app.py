from apistar.frameworks.wsgi import WSGIApp as App
from commands import commands
from components import components
from settings import settings
from routes import routes


app = App(
    routes=routes,
    components=components,
    commands=commands,
    settings=settings
)


if __name__ == '__main__':
    app.main()
