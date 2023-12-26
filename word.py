import random
import string
import sys


filename = "words.txt"
def read_file(filename):
    """
    Returns a list of words from a file.
    """
    try:
        f = open(filename, 'r')
        words = f.read().split()
        f.close()
        return words
    except IOError:
        print ("Error opening or reading input file: ", filename)
        sys.exit()

def match_letter_to_count(word):
    """
    Returns a dictionary of letters and their count.
    """
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
    weight = 10
    weighted_letters = {}
    for letter in range(10):
        weighted_letters[sorted_letters[letter]] = weight
        weight -= 1
    for letter in range(10, 26):
        weighted_letters[sorted_letters[letter]] = 0
    
    return weighted_letters

def score_word(word, weighted_letters):
    score = 0
    weights = weighted_letters
    
    for letter in word:
        if letter.isalpha():
            score += weights[letter]
            weights[letter] =0
    return score

def main():
    words = read_file(filename) #initialize words
    
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
    
    #assign weights to each letter from 10 to 0
    weighted_letters = assign_weights_to_letters(sorted_letters)

    sorted_letter_counts = sorted(letters, reverse=True)
    for index in range(len(sorted_letters)-1):
        print(sorted_letters[index], sorted_letter_counts[index])
    

    
    
main()