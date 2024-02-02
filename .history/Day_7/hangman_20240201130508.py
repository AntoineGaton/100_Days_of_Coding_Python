import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for _ in range(len(chosen_word)):
    display.append("_")
    
guess = input("Guess a letter: ").lower()

while _ in display:
   for letter in chosen_word:
      if letter == guess:
         for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                  display[position] = guess
      else:
        pass

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)