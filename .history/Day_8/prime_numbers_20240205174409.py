def prime_checker(number):
  is_Prime = True
  if (number == 1):
    is_Prime = False
  else:
    for i in range(2, number):
      if number%i == 0:
        is_Prime = False
        break
  if is_Prime:
    print("It's a prime number.")
  else:  
      print("It's not a prime number.")

def prime_number_printer(num):
   for number in range(1, num+1):
      prime_checker(number)
      print(f"{number} is a prime number.") if prime_checker(number) else print(f"{number} is not a prime number.")
n = int(input()) # Check this number
prime_checker(number=n)