"""
TODO:
1. Get all algos up to 866
2. Format file with algo.
"""

import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://projecteuler.net/problem=1'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
   # Parse the content of the response using BeautifulSoup
   soup = BeautifulSoup(response.text, 'html.parser')
   
   # Find all <p> tags in the content
   h2_tags = soup.find_all('h2')
   h3_tags = soup.find_all('h3')
   p_tags = soup.find_all('p')
   
   print('h2 tags:', h2_tags)
   print('h3 tags:', h3_tags)
   print('p tags:', p_tags)
   
   # Open a file to write the contents of <p> tags
   with open('project_euler_algos.txt', 'w', encoding='utf-8') as file:
      file.write======================================================================================================================================================n")
      
      file.write(f"Title:{h2_tags[0].text}")
      file.write('\n')
      
      file.write(h3_tags[0].text)
      file.write('\n')
      
      for p in p_tags:
         # Write each <p> content into the file
         file.write(p.text)
         file.write('\n')  # Add a newline to separate paragraphs
      file.write("======================================================================================================================================================\n\n\n")

   print('Content written to problem2_content.txt')
else:
   print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
