separator = "======================================================================================================================================================"
count = 0
# Open the source file in read mode
with open('project_euler_algos.txt', 'r', encoding='utf-8') as file:
   content = file.read()

groups = content.split(separator)

new_content = separator.join(groups[:121])
remaining_content = separator.join(groups[121:])

with open("text1.txt", "w", encoding="utf-8") as file:
   file.write(new_content)
   
with open("e")

print(new_content)


# 1,3,7,9