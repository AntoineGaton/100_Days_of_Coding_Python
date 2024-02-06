from blind_auction_art import logo
import os
print(logo)
bidders = []
print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
bidders.append({"name": name, "bid": bid})
is_True = True
while is_True:
   more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
   if more_bidders == "yes":
      os.system('clear')
      name = input("What is your name?: ")
      bid = int(input("What's your bid?: $"))
      bidders.append({"name": name, "bid": bid})
      