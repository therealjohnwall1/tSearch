import os

for filename in os.listdir('../util/storage'):
    os.remove('../util/storage/' + filename)