from blind_auction_art import logo
print(logo)
print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
is_True = True
while is_True:
   more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
   if more_bidders == "yes":
      