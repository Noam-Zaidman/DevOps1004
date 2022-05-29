from datetime import datetime
import requests


def url_caller(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is ok")


for url in ["http://github.com", "https://google.com", "https://moshe.com"]:
    url_caller(url)



def check_if_up(url):
    if requests.get(url).status_code == 200:
        print(f"{url} if up and running")
    else:
        print(f"sorry, {url} is down")


check_if_up("https://github.com")
