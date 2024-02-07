separator = "======================================================================================================================================================"
count = 0
# Open the source file in read mode
with open('project_euler_algos.txt', 'r', encoding='utf-8') as file:
   content = file.read()

groups = content.split(separator)

print(groups[9])

1