from flask import Flask, render_template

app = Flask(__name__)


def helper(*args):
    pass


@app.route("/")
def index():
    # return '<h1>Hello!</h1>'
    some_var = "Testing test"
    some_l = [1, 2, 3, 4, 5]
    some_d = {"name": "Alex", "age": 12}
    helper(
        "ewrewr",
        "erqerqer",
        "adfadfadf",
        "adfasdfasd",
        "dfadfasdfadf",
        "dafdadfdasdfasdfa",
        "adfadsfadfasdfasdf",
        "dafadfads",
    )
    return render_template(
        "index.html",
        temp_var=some_var,
        some_l=some_l,
        some_d=some_d,
        other_log_var_name_is_something_that=some_d,
    )


@app.route("/info")
def info():
    return "some info page"


@app.route("/user/<name>")
def user(name):
    return f"some user '{name}' page"


if __name__ == "__main__":
    app.run(debug=True)
