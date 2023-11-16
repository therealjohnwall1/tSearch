import os
from bs4 import BeautifulSoup
import mysql.connector
from setup import getConnection
import json
#make into a class so code for concurrency is clean

db = mysql.connector.connect( # conencting to host, change later
        host = "localhost",
        user = "root",
        passwd = "root", # change to actual password later
    )
cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS sites")
cursor.execute("USE sites")
cursor.execute("Create table if not exists siteinfo (title VARCHAR(100), data json")

path = "../util/storage"
storage = os.listdir(path)
fileList = []
for html_files in storage:
    fileObj = open(html_files, 'r')
    soup = BeautifulSoup(fileObj, 'html.parser')
    diction = {}
    diction["title"] = soup.title.name
    diction["links"] = []

    title = soup.title.name
    links = soup.find_all('a')
    for link in links:
       diction["links"].append(link.get('href'))
    diction["text"] = soup.get_text()
    json_data = json.dumps(diction)
    cursor.execute('insert into table values (%s, %s)', (title, json_data))

db.commit()
