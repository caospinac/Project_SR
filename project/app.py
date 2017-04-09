from jinja2 import Environment, PackageLoader
from sanic import Sanic
from sanic.response import html


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


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8000
    )
