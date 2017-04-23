from jinja2 import Environment, PackageLoader
from pony import orm
from sanic import Sanic
from sanic.exceptions import NotFound, FileNotFound
from sanic.response import html, json
# from sanic_cors import CORS
from sanic_session import InMemorySessionInterface

from config import database, server
from controllers import BaseController
from routes import api_routes
from models.base import engine


app = Sanic(__name__)
app.static("/", "./agronify/static/")
app.config.update(server)
app.config.update(database)

env = Environment(
    loader=PackageLoader("app", "templates"),
)

session_interface = InMemorySessionInterface()


@app.exception(NotFound, FileNotFound)
def ignore_404s(request, exception):
    return BaseController.response_status(404)


@app.middleware('request')
async def add_session_to_request(request):
    # before each request initialize a session
    # using the client's request
    await session_interface.open(request)


@app.middleware('response')
async def save_session(request, response):
    # after each request save the session,
    # pass the response to set client cookies
    await session_interface.save(request, response)


@app.route("/", methods=['GET', 'POST'])
async def index(request):
    view = env.get_template("building.html")
    html_content = view.render()
    return html(html_content)


@app.route("/home", methods=['GET', 'POST'])
async def home(request):
    view = env.get_template("base.html")
    html_content = view.render()
    return html(html_content)


for api_route in api_routes:
    # CORS(app)
    app.add_route(*api_route)


if __name__ == '__main__':
    orm.sql_debug(app.config.SQL_DEBUG)
    try:
        # engine.bind(app.config.DB_CLIENT, app.config.DB_NAME, create_db=True)
        engine.bind(
            'postgres',
            user=app.config.DB_USER,
            password=app.config.DB_PASSWORD,
            host=app.config.DB_HOST,
            database=app.config.DB_NAME
        )
    except Exception as e:
        pass
    else:
        engine.generate_mapping(create_tables=True)

    app.run(
        debug=app.config.DEBUG,
        host=app.config.HOST,
        port=app.config.PORT
    )
