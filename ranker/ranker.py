from indexer.grabber import database
def rank(userQuery):
    database = database()
    database.cursor.execute('select * from siteinfo')

        
    







