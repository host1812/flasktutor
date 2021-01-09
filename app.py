from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/report", methods=["POST"])
def report():
    username = request.form.get("username")
    report = {"isupper": False, "islower": False, "endswithnum": False}
    # for c in username:
    #     if c.isupper():
    #         report["isupper"] = True
    #     if c.islower():
    #         report["islower"] = True
    if any(c.isupper() for c in username):
        report["isupper"] = True
    if any(c.islower() for c in username):
        report["islower"] = True
    if username[-1] in [str(x) for x in range(10)]:
        report["endswithnum"] = True

    return render_template("report.html", username=username, report=report)


if __name__ == "__main__":
    app.run(debug=True)
