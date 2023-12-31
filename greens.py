from test import words
import string

def match_letter_to_count(words):
    letter_counts = {}
    for word in words:
        for letter in word:
            if letter.isalpha():
                letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

def create_column_list(words, index):
    column_list = []
    for word in words:
        if len(word) > index:
            letter = word[index]
            if letter.isalpha():
                column_list.append(letter)
    return column_list

def find_most_common_letters(column_list):
    letter_count = {}
    for letter in column_list:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_letter_count

def weight_columns(sorted_letter_count):
    total = sum(count for _, count in sorted_letter_count)
    weighted_columns = {letter: count / total for letter, count in sorted_letter_count}
    return weighted_columns

def weight_by_column(letters, columns, index):
    weighted_letters = {}
    for letter in letters:
        weighted_letters[letter] = letters.get(letter, 0) * columns.get(letter, 0)
    return weighted_letters

def score_word(word, weighted_letters):
    score = sum(weighted_letters[index].get(letter, 0) for index, letter in enumerate(word))
    return score

def greens(possible_words):
    letters = {}
    for letter in string.ascii_lowercase:
        letters[letter] = 0

    for word in possible_words:
        letter_count = match_letter_to_count([word])
        for letter in letter_count:
            letters[letter] += letter_count[letter]

    letters = dict(sorted(letters.items(), key=lambda x: x[1], reverse=True))

    columns = []
    weighted_columns = []

    for index in range(5):
        column = create_column_list(possible_words, index)
        sorted_column = find_most_common_letters(column)
        weighted_column = weight_columns(sorted_column)
        weighted_columns.append(weighted_column)

    best_word = ['', 0]
    for word in possible_words:
        weighted_letters = [weight_by_column(letters, column, index) for index, column in enumerate(weighted_columns)]
        word_score = score_word(word, weighted_letters)
        if word_score > best_word[1]:
            best_word = [word, word_score]

    return best_word