from jinja2 import Environment, PackageLoader
from pony import orm
from sanic import Sanic
from sanic.response import html
from sanic_cors import CORS

from routes import view_route_list
from models.base import engine


app = Sanic(__name__)
app.static("/static", "./static")
env = Environment(
    loader=PackageLoader("app", "views"),
)


@app.route("/", methods=['GET', 'POST'])
async def index(request):
    view = env.get_template("index.html")
    html_content = view.render(data="Hello world")
    return html(html_content)


for view_route in view_route_list:
    CORS(app)
    app.add_route(*view_route)


orm.sql_debug(True)

if __name__ == "__main__":
    engine.bind("sqlite", "database.sqlite", create_db=True)
else:
    engine.bind("sqlite", "test.sqlite", create_db=True)

engine.generate_mapping(create_tables=True)

app.run(
    debug=True,
    host="0.0.0.0",
    port=8000
)
