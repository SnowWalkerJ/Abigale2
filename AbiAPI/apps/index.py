from apistar.renderers import HTMLRenderer
from apistar import annotate


@annotate(renderers=[HTMLRenderer()])
def index():
    with open('web/index_prod.html') as f:
        return f.read()
