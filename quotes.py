from bs4 import BeautifulSoup
import requests
import time

source = requests.get('http://edlester.com/17-short-positive-quotes-will-brighten-day/').text
time.sleep(4)
soup = BeautifulSoup(source, 'lxml')

for b in soup.findAll("h3", {"style": "text-align: center;"}):
    print(b.text)