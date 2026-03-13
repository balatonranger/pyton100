#hangman
import random
#todo 1. Create a list of words to choose from.
word_list = ["hello", "world", "python", "programming"]
chosen_word = random.choice(word_list)
print(chosen_word)
#todo 2. Create an empty list to store the letters that have been guessed.
placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "-"
print(placeholder)

guess = input("Guess a letter: ").lower()
print(guess)
#todo 3. Check if the guessed letter is in the chosen word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")