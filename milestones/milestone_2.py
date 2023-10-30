import random


fruit_word_list = ['mango', 'apple','kiwi', 'lemon', 'orange']
random_fruit_selection = random.choice(word_list)

print(fruit_word_list)
print(random_fruit_selection)

guess = input("Enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print('good guess')
else:
    print("Oops! That is not a valid input.")
