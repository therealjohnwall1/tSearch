import os
from bs4 import BeautifulSoup
import mysql.connector
from setup import getConnection
import json
#make into a class so code for concurrency is clean

class database:
    def __init__(self):
        self.db = mysql.connector.connect( # conencting to host, change later
                host = "127.0.0.1",
                user = "root",
                passwd = "6241", # change to actual password later
        )

        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS sites")
        self.cursor.execute("USE sites")
        self.cursor.execute("Create table if not exists siteinfo (title VARCHAR(100), data json")
    
    def writeToDB(self): # only run when updating or starting
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
            self.cursor.execute('insert into table values (%s, %s)', (title, json_data))
        self.db.commit()
