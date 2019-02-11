import requests
from bs4 import BeautifulSoup


request = requests.get("https://github.com/")
if request.status_code == 200 :
    print("Request was successful to " + request.url)
    source = request.text
    soup = BeautifulSoup(source)
    for x in soup.find_all("a"):
        print(x)
else:
    print("Invalid request"+ request.url)