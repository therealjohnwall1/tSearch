import os
from bs4 import BeautifulSoup

path = "../util/storage"

files = os.listdir(path)
fileList = []
for i in files:
    path = os.path.join(path,i)
    fileObj = open(path, 'r')
    soup = BeautifulSoup(fileObj, 'html.parser')

    print(soup.title.name)
    fileObj.close()



