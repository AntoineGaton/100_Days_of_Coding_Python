"""
To Do:
1. FIX WHILE LOOP! MADE 2000 FILES. 
"""

import os
separator = "======================================================================================================================================================"
page = 0
file_path = "project_euler_algos.txt"

def is_file_empty(file_path):
   # Check if the file is empty or contains only whitespace
   with open(file_path, 'r', encoding='utf-8') as file:
      return not file.read().strip()

is_empty = is_file_empty(file_path)
while not is_empty:
   # Open the source file in read mode
   with open('project_euler_algos.txt', 'r', encoding='utf-8') as file:
      content = file.read()
      

   groups = content.split(separator)

   new_content = separator.join(groups[:121])
   remaining_content = separator.join(groups[121:])

   with open(f"text{page}.txt", "w", encoding="utf-8") as file:
      file.write(new_content)
      
   with open("project_euler_algos.txt", "w", encoding="utf-8") as file:
      file.write(remaining_content)
   
   page += 1
   

os.remove("project_euler_algos.txt")