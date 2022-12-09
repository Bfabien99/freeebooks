from flask import Flask, request, render_template, redirect, url_for
import urllib.request, json

# initialisation de flask
app = Flask(__name__)


# Creation des routes
@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/books', methods=["GET"])
def books():
    url = "http://localhost:5000/books"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    books=dict["result"]
    return render_template("book.html",books=books)


if __name__=='__main__':
    app.run()