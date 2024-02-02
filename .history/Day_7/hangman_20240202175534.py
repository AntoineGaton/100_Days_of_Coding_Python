"""
THINGS TO DO:
1. Quicker way to find an easy word.
2. Add a way to play again.
3. Add a way to quit the game.
4. Custom game board.
6. Add custom words using a file.
7. If letter is already guessed, don't decrement lives.
8. Add a way to show the letters that have been guessed.
9. Create a executable file.

"""
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
      if difficulty == 1 and len(word) <= 5:
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
   
   print(display)
   return display
   
def game_logic(display, rand_word, lives):

   while "_" in display and lives > 0:  # Check if lives are more than 0 as well
      guess = input("Guess a letter: ").lower()
      if guess in rand_word:  # Check if the guessed letter is in the word
         for position, letter in enumerate(rand_word):
               if letter == guess:
                  display[position] = guess  # Reveal the letter in the display
      else:
         lives -= 1  # Decrement lives if the guess is wrong
         if lives == 0:
               print("You lose!")
               print(f"The word was {rand_word}.")  # Reveal the word at the end
               time.sleep(5)
               return  # Exit the function, the game is over
      print(f"You have {lives} lives left!")
      print(display)
   
   if lives > 0:
      print("You win!")
   else:
      print("You lose!")
   
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

if __name__ == "__main__":
   main()