from flask import Flask, render_template, request
from scraping import web_scraper

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=["POST", "GET"])
def search_result():
    if(request.method == "POST"):
        results = []
        query = request.form.get("key")
        web_scraper(query, results)
        return render_template("display.html", results=results)


if __name__ == '__main__':
    app.run(debug=True)
