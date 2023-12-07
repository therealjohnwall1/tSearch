import os

for filename in os.listdir('../indexer/storage/'):
    os.remove('../indexer/storage/' + filename)