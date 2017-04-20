from jinja2 import Environment, PackageLoader
from pony import orm
from sanic import Sanic
from sanic.exceptions import NotFound, FileNotFound
from sanic.response import html, json
from sanic_cors import CORS

from config import database, server
from controllers import BaseController
from routes import view_route_list
from models.base import engine


app = Sanic(__name__)
app.static("/", "./agronify/static/")
app.config.update(server)
app.config.update(database)

env = Environment(
    loader=PackageLoader("app", "views"),
)


@app.exception(NotFound, FileNotFound)
def ignore_404s(request, exception):
    return BaseController.response_status(404)


@app.route("/", methods=['GET', 'POST'])
async def index(request):
    view = env.get_template("base.html")
    html_content = view.render()
    return html(html_content)


for view_route in view_route_list:
    CORS(app)
    app.add_route(*view_route)


if __name__ == '__main__':
    orm.sql_debug(app.config.SQL_DEBUG)
    try:
        engine.bind(app.config.DB_CLIENT, app.config.DB_NAME, create_db=True)
    except Exception as e:
        pass
    else:
        engine.generate_mapping(create_tables=True)

    app.run(
        debug=app.config.DEBUG,
        host=app.config.HOST,
        port=app.config.PORT
    )
