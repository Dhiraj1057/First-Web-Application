import flask
import datetime

date = datetime.datetime.now()

app = flask.Flask(__name__)


@app.route("/")
def home():
    return flask.render_template("index.html", year=date.year)


@app.route("/login.html")
def login():
    return flask.render_template("login.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
