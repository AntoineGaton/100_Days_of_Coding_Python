separator = "======================================================================================================================================================"
count = 0
# Open the source file in read mode
with open('project_euler_algos.txt', 'r', encoding='utf-8') as file:
   content = file.read()

groups = content.split(separator)

new_content = separator.join(groups[0])

for i in new_content:
   print(i)



# 1,3,7,9