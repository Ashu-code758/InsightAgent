from flask import Flask, render_template, send_from_directory, send_file, request
from agents.planner import Planner
from agents.executor import Executor
import os

app = Flask(__name__)

planner = Planner()
executor = Executor()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/download/csv")
def download_csv():
    return send_file("data/books.csv", as_attachment=True)


@app.route("/download/pdf")
def download_pdf():
    return send_file("reports/report.pdf", as_attachment=True)


@app.route("/charts/<path:filename>")
def charts(filename):
    return send_from_directory("charts", filename)


@app.route("/analyze", methods=["POST"])
def analyze():

    try:
        url = request.form["url"]

        plan = planner.plan(
            "Analyze this website and generate business insights."
        )

        result = executor.execute(plan, url)

        return render_template(
            "result.html",
            analysis=result["analysis"]
        )

    except Exception as e:
        return f"<h2>Error:</h2><pre>{str(e)}</pre>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)