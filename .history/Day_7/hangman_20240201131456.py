import random
from 
import os


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

def clear_screen():
   if os.name == 'nt':
      os.system('cls')
   else:
      os.system('clear')
      
def game_board():
   display = []

   for _ in range(len(chosen_word)):
      display.append("_")
   return display
   
def game_logic(display):
   while "_" in display:   
      guess = input("Guess a letter: ").lower()
      for letter in chosen_word:
         if letter == guess:
            for position in range(len(chosen_word)):
               if chosen_word[position] == guess:
                     display[position] = guess   
   
def main():
   #Testing code
   print(f'Pssst, the solution is {chosen_word}.')
   clear_screen()
   display = game_board()
   game_logic(display)
   print(display)
   print("You win!")

if __name__ == "__main__":
   main()