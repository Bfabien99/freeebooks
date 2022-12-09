from flask import Flask, request, render_template, redirect, url_for

# initialisation de flask
app = Flask(__name__)


# Creation des routes
@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


if __name__=='__main__':
    app.run()