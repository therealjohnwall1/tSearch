import csv

def move():
    with open("Free_Proxy_List.csv", "r") as proxiesFile:
        reader = csv.DictReader(proxiesFile)
        next(reader)
        for p in reader:
            print(p["ip"])
            with open('proxies.txt', 'a') as file:
            # Write content to the file
                file.write(p["ip"] + '\n')
