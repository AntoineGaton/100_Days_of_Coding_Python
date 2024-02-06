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
    print(f"{number} IS a prime number.")
  else:  
      print(f"{number} is NOT a prime number.")

def prime_number_printer(num):
   for number in range(1, num+1):
      prime_checker(number)
      
print("Welcome to the Prime Number Checker!")

while True:
   choice = input("Do you want to check a single number or a range of numbers? (single/range): ").lower()

   if choice == "single":
      n = int(input()) # Check this number
      prime_checker(number=n)
      break

   elif choice == "range":
      n = int(input("Enter the range of numbers: "))
      prime_number_printer(n)

   else:
      print("Invalid input")