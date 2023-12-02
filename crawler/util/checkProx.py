import threading
import queue
import requests
import csv
import random

class ProxyChecker:
    def __init__(self):
        self.q = queue.Queue()
        self.validProxies = []
        self.threads = []
        self.runner()
        
    def checkProxy(self):
        while not self.q.empty():
            proxy = self.q.get()
            try:
                r = requests.get("http://ipinfo.io/json", proxies={"https": proxy, "https:": proxy}, timeout=5)
            except:
                print(r.status_code)
                pass
            if r.status_code == 200:
                    self.validProxies.append(proxy)
                    print(f"Code:{r.status_code}")
    def runner(self):
        with open("Free_Proxy_List.csv", "r") as proxiesFile:
            reader = csv.reader(proxiesFile)
            for p in reader:
                self.q.put(p)

        self.threads = [threading.Thread(target=self.checkProxy) for _ in range(10)]
        for thread in self.threads:
            thread.start()

        # Wait for all threads to finish
        for thread in self.threads:
            thread.join()

    def getProxy(self):
        x = random.randint(0, len(self.validProxies)-1)
        return self.validProxies[x]


g = ProxyChecker()
x = g.getProxy()

r = requests.get("http://books.toscrape.com/", proxies={"https": x, "https:": x}, timeout=5)
print(r.status_code)