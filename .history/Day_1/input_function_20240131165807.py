# Provide any name in the input pane below.
# That value can be accessed using the input() function.
# Don't put anything inside the input() function!
def num_letters(name):
  count = 0
  for i in name:
    count+=1
  print(count)

name = input()

num_letters(name)