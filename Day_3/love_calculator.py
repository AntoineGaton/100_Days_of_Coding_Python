print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
def calculate_love_score(name1, name2):
    combined_names = name1.lower() + name2.lower()
    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")
    love_score = int(f"{true_count}{love_count}")
    return love_score

def love_calculator(name1, name2):
    score = calculate_love_score(name1, name2)
    
    if score < 10 or score > 90:
        return f"Your score is {score}, you go together like coke and mentos."
    elif 40 <= score <= 50:
        return f"Your score is {score}, you are alright together."
    else:
        return f"Your score is {score}."


result = love_calculator(name1, name2)

print(result)