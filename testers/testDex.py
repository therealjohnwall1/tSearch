from pathlib import Path
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.analysis import StemmingAnalyzer
from whoosh.index import open_dir
import os.path
import os

if not os.path.exists("/testIndex"):
    stem_ana= StemmingAnalyzer()
    os.makedirs("../testIndex", exist_ok=True)
    schema = Schema(title=TEXT(stored=True), content=TEXT,
                path=ID(stored=True), tags=KEYWORD, icon=STORED)
    ix = create_in("../testIndex", schema)
else:
    ix = open_dir("../testIndex")

writer = ix.writer()
writer.add_document(title=u"My document", content=u"This is my document!",
                    path=u"/a", tags=u"first short", icon=u"/icons/star.png")
writer.add_document(title=u"Second try", content=u"This is the second example.",
                    path=u"/b", tags=u"second short", icon=u"/icons/sheep.png")
writer.add_document(title=u"Third time's the charm", content=u"Examples are many.",
                    path=u"/c", tags=u"short", icon=u"/icons/book.png")
writer.commit()



# def writeToIndex(writer):
#     global x
#     writer.add_document(title=u"Test Title",
#                         headers=u"Test Headers",
#                         content=u"Test Content",
#                         url=u"Test URL {x}")
#     x+=1
#     writer.commit()

# writeToIndex(ix.writer())
# writeToIndex(ix.writer())
# writeToIndex(ix.writer())
# writeToIndex(ix.writer())