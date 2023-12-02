import mysql.connector
# from setup import getConnection

db = mysql.connector.connect( # conencting to host, change later
        host="127.0.0.1",
        port="3306",
        user="root",
        password="6241",
        database="searcheng"
        )