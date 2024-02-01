# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
def is_leap_year(year):
    # A year is a leap year if it is divisible by 4
    if year % 4 == 0:
        # Except if it is divisible by 100, it is not a leap year
        if year % 100 == 0:
            # However, if it is divisible by 400, it is a leap year
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Determine if it is a leap year or not
if is_leap_year(year):
    print("Leap year")
else:
    print("Not leap year")

'''
# Which year do you want to check?
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
'''