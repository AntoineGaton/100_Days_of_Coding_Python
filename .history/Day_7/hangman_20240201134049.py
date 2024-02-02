from random_word import RandomWords
import random
import os
import time

def clear_screen():
   if os.name == 'nt':
      os.system('cls')
   else:
      os.system('clear')

def difficulty_setting():
   while True:
      difficulty = input("Choose difficulty: easy, medium, hard: ").lower()
      if difficulty == "easy":
         lives = 10
         return 1, lives
      elif difficulty == "medium":
         lives = 5
         return 2, lives
      elif difficulty == "hard":
         lives = 3
         return 3, lives
      else:
         print("Invalid input")
      
def random_word(difficulty):
   r = RandomWords()
   while True:
      word = r.get_random_word()
      print("Looking for a word...")
      time.sleep(1)
      if difficulty == 1 and len(word) < 4:
         print("Found an easy word!")
         return word
      elif difficulty == 2 and len(word) >= 6 and len(word) <= 8:   
         print("Found an medium word!")
         return word
      elif difficulty == 3 and len(word) > 8:
         print("Found an hard word!")
         return word

def game_board(rand_word):
   display = []

   for _ in range(len(rand_word)):
      display.append("_")
   return display
   
def game_logic(display, rand_word, lives):
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
   print("=====================")
   print("Welcome to Hangman!")
   print("=====================")
   difficulty, lives = difficulty_setting()
   print(f"You have {lives} lives!")
   rand_word = random_word(difficulty)
   display = game_board(rand_word)
   game_logic(display, rand_word, lives)
   print("You win!")

if __name__ == "__main__":
   main()