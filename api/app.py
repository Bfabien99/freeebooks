from flask import Flask, request, jsonify
import pymysql
import os

# initialisation de flask
app = Flask(__name__)

# Function pour se connecter à la BD
def db_connection():
    conn = None
    try:
        conn = pymysql.connect(host="127.0.0.1",port=3306,database="freeebooks",user="root",password="password",cursorclass=pymysql.cursors.DictCursor)
    except pymysql.error as e:
        print(e)
    return conn

# Creation des routes
@app.route('/books', methods=["GET", "POST"])
def books():
    error = False
    conn = db_connection()
    cursor = conn.cursor()
    
    if request.method == "GET":
        cursor.execute("SELECT * FROM books")
        results=cursor.fetchall()
        
        if results is not None:
            message = "all books"
            return jsonify(dict(message=message,error=error,result=results)),200
        else:
            message = "no books found"
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