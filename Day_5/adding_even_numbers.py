target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum = 0
for i in range(1, target+1):
  if i%2 == 0:
    sum +=i

"""
Alternative solution:
even_sum = 0
for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)
"""


print(sum)