from whoosh.index import open_dir
import os.path
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser


schema = Schema(title=TEXT(stored=True),content=TEXT)
paf = "test"

if not os.path.exists(paf):
    print("DNE")
    os.mkdir(paf)
    ix = create_in(paf, schema)
else:
    ix = open_dir(paf)
    print("exists")
#creates index in paf using schema
# writer = ix.writer()
# writer.add_document(title=u"First document", content=u"This is the first document we've added!")
# writer.add_document(title=u"Second document", content=u"The second one is even more interesting!")

# writer.commit()


with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("second")
    results = searcher.search(query)
    print(results[0])