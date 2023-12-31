import random
from test import words
from greens import greens
import copy
from concurrent.futures import ThreadPoolExecutor

def validate_guess(guess, answer):
    validated_letters = {'yellows': set(), 'greys': set(), 'greens': {}}
    
    for i, letter in enumerate(guess):
        if letter in answer:
            if answer[i] == letter:
                validated_letters['greens'][i] = letter
            else:
                validated_letters['yellows'].add(letter)
        else:
            validated_letters['greys'].add(letter)

    return validated_letters

def narrow_down_words(validated_letters, possible_words):
    filtered_words = []
    with ThreadPoolExecutor(max_workers = 10) as executor:
        for word in possible_words:
            if all(word[i] == letter for i, letter in validated_letters['greens'].items()) and \
            validated_letters['yellows'].issubset(set(word)) and \
            not any(letter in word for letter in validated_letters['greys']):
                filtered_words.append(word)

    return filtered_words


def algorithm(possible_words, answer_word, first_guess):
    guess = first_guess
    guesses = 1

    while guess != answer_word:
        validated_letters = validate_guess(guess, answer_word)

        possible_words = narrow_down_words(validated_letters, possible_words)

        guesses += 1

        if not possible_words:
            print("No possible words left. Is the answer word in the word list?")
            break
        guess = greens(possible_words)[0]
        if guess in possible_words:
            possible_words.remove(guess)
    
    return guesses

guesses = 0
possible_words = words.copy()
first_guess = 'salet'  # example first guess
sample_answer_1 = 'hello'
sample_answer_2 = 'world'

guesses = algorithm(possible_words, sample_answer_1, first_guess)
print(f"Total guesses: {guesses}")
guesses = algorithm(possible_words, sample_answer_2, first_guess)
print(f"Total guesses: {guesses}")


