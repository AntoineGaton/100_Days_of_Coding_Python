from pprint import pprint
import requests
from bs4 import BeautifulSoup

url ='https://www.nba.com/stats/players'

response = requests.get(url)

if response.status_code == 200:
   soup = BeautifulSoup(response.text, 'html.parser')
   
   tag_info = soup.find_all(class_='Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL')
   
   for tag in tag_info:
      print(tag.text)