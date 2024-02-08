from pprint import pprint
import requests
from bs4 import BeautifulSoup

url ='https://www.nba.com/stats/players'

response = requests.get(url)

if response.status_code == 200:
   soup = BeautifulSoup(response.text, 'html.parser')
   
   tag_info = soup.find_all('tbody', class_='nba-stat-table__body')
   
   print(tag_info)