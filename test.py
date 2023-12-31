import sys


def read_file(filename):
    """
    Returns a list of words from a file.
    """
    try:
        with open(filename, 'r') as f:
            words = f.read().lower().split()
        return words
    except IOError:
        print("Error opening or reading input file: ", filename)
        sys.exit()

def score_word(guess_word, answer_word):
    """
    Scores the guess_word against the answer_word.
    """
    green_score = 3
    yellow_score = 1
    score = 0

    guess_letters = set(guess_word)
    answer_letters = set(answer_word)
    common_letters = guess_letters.intersection(answer_letters)

    # Score greens
    for i in range(len(guess_word)):
        if guess_word[i] == answer_word[i]:
            score += green_score
            common_letters.discard(guess_word[i])  

    # Score yellows
    score += yellow_score * len(common_letters)

    return score

def validate_word_score(guess_word, words):
    total_score = sum(score_word(guess_word, word) for word in words)
    return total_score / len(words)

def main():
    global words
    words = read_file("words.txt")

main()