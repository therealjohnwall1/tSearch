from whoosh.index import open_dir
import os.path, os
from whoosh.index import create_in
from whoosh.qparser import QueryParser
from whoosh import index
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
qry = input("Enter a query: ")

path = "testIndex"
ix = open_dir(path)
if(os.path.exists(path)):
    ix = open_dir(path)
    parser = QueryParser("content", ix.schema)
    myquery = parser.parse(qry)
    with ix.searcher() as searcher:
        results = searcher.search(myquery)
        print(results[0])
else:
    print("index dne")