import random
import os

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

def clear_screen():
   if os.name == 'nt':
      os.system('cls')
   else:
      
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for _ in range(len(chosen_word)):
    display.append("_")
    

while "_" in display:   
   guess = input("Guess a letter: ").lower()
   for letter in chosen_word:
      if letter == guess:
         for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                  display[position] = guess
   
   print(display)

print("You win!")