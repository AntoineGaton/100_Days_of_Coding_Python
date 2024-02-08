from pprint import pprint
import requests
from bs4 import BeautifulSoup

url ='https://www.nba.com/stats/players'

response = requests.get(url)

if response.status_code == 200:
   soup = BeautifulSoup(response.text, 'html.parser')
   
   tag_info = soup.find_all('div', class="LeaderBoardCard_lbcWrapper__e-6bCZ px-3 w-full sm:w-1/2 sm:px-4 lg:w-1/3  LeaderBoardCard_leaderBoardCategory__vWRuZ')
   
   print(tag_info)