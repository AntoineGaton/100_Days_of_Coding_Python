from random_word import RandomWords
import random
import os

r = RandomWords()
rand_word = r.get_random_word()

def clear_screen():
   if os.name == 'nt':
      os.system('cls')
   else:
      os.system('clear')
      
def game_board():
   display = []

   for _ in range(len(rand_word)):
      display.append("_")
   return display
   
def game_logic(display):
   while "_" in display:   
      guess = input("Guess a letter: ").lower()
      for letter in rand_word:
         if letter == guess:
            for position in range(len(rand_word)):
               if rand_word[position] == guess:
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