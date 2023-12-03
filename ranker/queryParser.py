from whoosh.index import open_dir
import os.path
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser

qry = input("Enter a query: ")

path = "../indexer/theINDEX"

if(os.path.exists(path)):
    ix = open_dir(path)
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(qry)
        results = searcher.search(query)
        print(results[0])