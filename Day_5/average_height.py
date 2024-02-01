# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total = 0
num_students = 0

for i in student_heights:
  total += i
  num_students += 1

avg_height = round(total/num_students)

print(f"total height = {total}")
print(f"number of students = {num_students}")
print(f"average height = {avg_height}")
