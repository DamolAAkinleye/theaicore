import random 


def check_guess(guess: str):
    guess_lower  = guess.lower()
    return guess_lower.isalpha() and len(guess_lower)== 1 and guess_lower in word

def ask_for_input():
    while True:
        print(word)
        guess = input("Guess a letter:  ")
        if len(guess) == 1  and guess.isalpha():
            break 
    
    if check_guess(guess):
        print(f"Good guess! {guess} is in the {word}.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

word = random.choice(['apple', 'lemon','mango'])
ask_for_input()