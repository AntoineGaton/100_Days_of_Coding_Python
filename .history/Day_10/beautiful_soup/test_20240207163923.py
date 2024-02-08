import requests
from bs4 import BeautifulSoup

url ='https://www.nba.com/stats/'

response = requests.get(url)
