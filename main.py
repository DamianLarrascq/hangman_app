import random
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in words or ' ' in words:
        word = random.choice(words)

    return word.upper()

