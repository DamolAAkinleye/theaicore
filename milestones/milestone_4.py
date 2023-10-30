import random 

class Hangman:
    
    def __init__(self, word_list , num_lives = 5):
        self.word_list  = word_list
        self.num_lives  = num_lives
        self.word  = random.choice(word_list)
        self.word_guess = ("_ "* len(self.word)).split()
        self.list_of_guesses = []
        self.num_letters = len(set(list(self.word)))
        
        
    def __check_guess(self, guess:str):
        print(self.word)
        guess_lower = guess.lower()
        if  guess_lower in self.word: 
            print(f"Good guess! {guess_lower} is in the word.")
            for index, character in enumerate(self.word):
                if character == guess_lower:
                    self.word_guess[index] = character
            self.num_letters -= 1
            
        else:
            num_lives -= 1
            print(f"Sorry, {guess_lower} is not in the word")
            print(f"ou have {self.num_lives} lives left.")
        
    def ask_for_input(self):
        while True :
            guess  = input("Guess a letter: ")
            if len(guess) != 1:
                print("invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.__check_guess(guess)
                self.list_of_guesses.append(guess)
                

h = Hangman(["apple","mango"])
h.ask_for_input()