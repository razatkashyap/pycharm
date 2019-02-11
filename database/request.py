import requests
from bs4 import BeautifulSoup
response = requests.post("http://127.0.0.1:5000/user/", {"name" : "jhdk"})
print(response.text)