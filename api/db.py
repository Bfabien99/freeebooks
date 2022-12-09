import os
import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password=os.getenv("DB_PASSWORD"),database="freeebooks", cursorclass=pymysql.cursors.DictCursor)

mycursor = conn.cursor()

# Création de la BD
# sql = "CREATE DATABASE IF NOT EXISTS freeebooks"

# Création des TABLES
'''
sql = """CREATE TABLE IF NOT EXISTS books(
    id int PRIMARY KEY AUTO_INCREMENT,
    cover text,
    title varchar(100) NOT NULL,
    description text NOT NULL,
    view int,
    category text NOT NULL,
    published_at datetime default CURRENT_TIMESTAMP
    )"""
'''

# Création d'un index
# sql = "CREATE UNIQUE INDEX ubook ON books (title)"
# mycursor.execute(sql)
conn.close