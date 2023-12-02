from pathlib import Path
import requests
import threading

# rembr to add proxy later on when sending rq

# file = "prat.txt"
fullLinks = open("top1kFullLinks.txt", "a")
with open("top-1000-websites.txt", "r") as links:
    urls = [site.strip() for site in links.readlines()]


for site in urls:
    try:
        site = "https://" + site
        r = requests.get(site)
        print(r.status_code)
        fullLinks.write(site + "\n")

    except:
        try:
            site = "http://" + site
            r = requests.get(site)
            print(r.status_code)
            fullLinks.write(site + "\n")
        except:
            print(f"{site} site failed")
            continue
        
links.close()
