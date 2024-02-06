from blind_auction_art import logo
import os

def print_logo():
   print(logo)

def get_bidder_info():
   name = input("What is your name?: ")
   bid = int(input("What's your bid?: $"))
   return {"name": name, "bid": bid}

def main():
   bidders = []
   
   bidder = get_bidder_info()
   bidders.append(bidder)
   
   is_True = True
   
   while is_True:
      more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
      if more_bidders == "yes":
         if os.name == "nt":
            os.system('cls')
            
         os.system('clear')
         name = input("What is your name?: ")
         bid = int(input("What's your bid?: $"))
         bidders.append({"name": name, "bid": bid})
      else:
         is_True = False
   highest_bid = bidders[0]["bid"]
   winner = bidders[0]["name"]
   for bidder in bidders:
      if bidder["bid"] > highest_bid:
         highest_bid = bidder["bid"]
         winner = bidder["name"]
   print(f"The winner is {winner} with a bid of ${highest_bid}.")
   
if __name__ == "__main__":
   print_logo()
   print("Welcome to the secret auction program.")
   main()