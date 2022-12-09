from flask import Flask, request, jsonify

# initialisation de flask
app = Flask(__name__)


# Creation des routes
@app.route('/books', methods=["GET", "POST"])
def books():
    if request.method == "GET":
        message = "GET"
        error = False
        return jsonify(dict(message=message,error=error,result=[])),200
    
    if request.method == "POST":
        message = "POST"
        error = False
        return jsonify(dict(message=message,error=error,result=[])),200

    return jsonify(dict(message="Method not allowed",error=True,result=[])), 405


@app.route('/categories', methods=["GET", "POST"])
def categories():
    if request.method == "GET":
        message = "GET"
        error = False
        return jsonify(dict(message=message,error=error,result=[])),200
    
    if request.method == "POST":
        message = "POST"
        error = False
        return jsonify(dict(message=message,error=error,result=[])),200

    return jsonify(dict(message="Method not allowed",error=True,result=[])), 405
    
    
if __name__ == '__main__':
    app.run()