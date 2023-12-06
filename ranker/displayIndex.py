from whoosh.index import open_dir
from whoosh.query import Every 

ix = open_dir(".../testers/testIndex")
print(ix.schema)

results = ix.searcher().search(Every("content")) 

for result in results:
    print(f"title: {result.title} \nurl: {result.url} \nheaders: {result.headers} \ncontent: {result.content} \n")