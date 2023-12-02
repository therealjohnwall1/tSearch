import requests

websites = [
    "google.com",
    "facebook.com",
    "youtube.com",
    "baidu.com",
    "yahoo.com",
    "amazon.com",
    "wikipedia.org",
    "qq.com"
]

for site in websites:
    try:
        site = "https://" + site
        r = requests.get(site)
        print(r.status_code)
    except:
        print(f"Site {site} failed")
        continue

# r = requests.get("https://marriott.com")
# print(r.status_code)