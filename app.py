from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.get("/")
def index():
    """
    TODO: Render the home page provided under templates/index.html in the repository
    """
    return render_template("index.html")


@app.get("/search")
def search():

    """

    1. Capture the word that is being searched
    2. Seach for the word on Google and display results
    """

    args = request.args.get("q")
    return redirect(f"https://google.com/search?q={args}")


@app.get("/lucky_search")
def lucky_search_impl():
    """implementing lucky search button myself"""
    args2 = request.args.get("lucky")
    return redirect(f"https://google.com/search?lucky={args2}")

if __name__ == "__main__":
    app.run()
