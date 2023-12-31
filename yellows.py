import random
import string
from test import words, read_file, validate_word_score
#Returns a dictionary of letters and their count.
def match_letter_to_count(word):
    letter_count = {}
    for letter in word:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count


def find_letter_by_value(value):
    for letter in string.ascii_lowercase:
        if globals()[letter] == value:
            return letter

def assign_weights_to_letters(sorted_letters, sorted_letter_values):
    weighted_letters = {}    
    for i in range(len(sorted_letters)):
        weighted_letters[sorted_letters[i]] = sorted_letter_values[i]
    return weighted_letters

def score_word(word, weighted_letters):
    score = 0
    weights = weighted_letters
    
    for letter in word:
        if letter.isalpha():
            score += weights[letter]
            weights[letter] =0
    return score

def find_best_word(words, weighted_letters):
    scored_words = []
    for word in words:
        weights = weighted_letters.copy()
        scored_words.append((word, score_word(word, weights)))
    return scored_words

def adjust_weights(weighted_letters, word):
    weights = weighted_letters.copy()
    for letter in word:
        if letter.isalpha():
            weights[letter] = 0
    return weights

def yellows(words):
    
    
    #initialize letter counts
    for word in words:
        letter_count = match_letter_to_count(word)
        for letter in string.ascii_lowercase:
            if letter_count.get(letter, 0) > 0:
                globals()[letter] = globals().get(letter, 0) + letter_count[letter]
    letters = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    

    
    #sort letters by count from greatest to least
    sorted_letters= []
    for value in sorted(letters, reverse=True):
        sorted_letters.append(find_letter_by_value(value))
    
    #assign weights to each letter corresponding to how many occurrences it has in the list of words
    weighted_letters_1 = assign_weights_to_letters(sorted_letters, sorted(letters, reverse=True))
    

    # find best first word
    best_first_word = max(find_best_word(words, weighted_letters_1), key=lambda x: x[1])
    
    #adjust weights for second word
    weighted_letters_2 = adjust_weights(weighted_letters_1, best_first_word[0])
    
    #find best second word
    best_second_word = max(find_best_word(words, weighted_letters_2), key=lambda x: x[1])
    
    #adjust weights for third word
    weighted_letters_3 = adjust_weights(weighted_letters_2, best_second_word[0])
    
    #find best third word
    best_third_word = max(find_best_word(words, weighted_letters_3), key=lambda x: x[1])
    
    #adjust weights for fourth word
    weighted_letters_4 = adjust_weights(weighted_letters_3, best_third_word[0])
    
    #find best fourth word
    best_fourth_word = max(find_best_word(words, weighted_letters_4), key=lambda x: x[1])
    
    #adjust weights for fifth word
    weighted_letters_5 = adjust_weights(weighted_letters_4, best_fourth_word[0])
    best_fifth_word = max(find_best_word(words, weighted_letters_5), key=lambda x: x[1])
    
    
    
    print("Best first word: ", best_first_word)
    print("Best second word: ", best_second_word)
    print("Best third word: ", best_third_word)
    print("Best fourth word: ", best_fourth_word)
    print("Best fifth word: ", best_fifth_word)
    
    return best_first_word
    
yellows(words)