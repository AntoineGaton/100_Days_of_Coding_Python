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

print(display)