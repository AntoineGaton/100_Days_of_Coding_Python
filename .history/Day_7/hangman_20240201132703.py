from random_word import RandomWords
import random
import os

def clear_screen():
   if os.name == 'nt':
      os.system('cls')
   else:
      os.system('clear')
      
def random_word():
   r = RandomWords()
   word = r.get_random_word()
   return word

def difficulty_setting():
   while True:
      difficulty = input("Choose difficulty: easy, medium, hard: ").lower()
      if difficulty == "easy":
         return 3
      elif difficulty == "medium":
         return 2
      elif difficulty == "hard":
         return 1
      else:
         print("Invalid input")
      
def game_board(rand_word):
   display = []

   for _ in range(len(rand_word)):
      display.append("_")
   return display
   
def game_logic(display, rand_word):
   while "_" in display:   
      guess = input("Guess a letter: ").lower()
      for letter in rand_word:
         if letter == guess:
            for position in range(len(rand_word)):
               if rand_word[position] == guess:
                     display[position] = guess 
      print(display)    
   
def main():
   clear_screen()
   rand_word = random_word()
   print("=====================")
   print("Welcome to Hangman!")
   print("=====================")
   difficulty = difficulty_setting()
   display = game_board()
   game_logic(display, rand_word)
   print("You win!")

if __name__ == "__main__":
   main()