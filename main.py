import random
from words import words as mywords
import string


def get_valid_word(words):
    word = random.choice(words)     #chooses random letter from words file
    while '-' in words or ' ' in words:     #iterates through words until it finds a word without dash or space
        word = random.choice(words)     #inserts word from file to variable word

    return word.upper()     #returns the word in uppercase


def hangman():
    word_sel = get_valid_word(mywords)      #stores the chosen word
    word_letters = set(word_sel)        #divides word into separate letters
    alphabet = set(string.ascii_uppercase)  #english alphabet
    used_letters = set()        #variable storing the letters already used by the player
    user_input = input('Type letter: ').upper()
    word_list = [letter if letter in used_letters else '-' for letter in word_sel]      #show what current word is, show '-' for letters not guessed yet

    while len(word_letters) > 0:
        print('You have used these letters: ', ''.join(used_letters))

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
        elif user_input in used_letters:
            print('Letter already used')
        else:
            print('Invalid character')


