from test import validate_word_score, words
import numpy as np

def main():
    scores = np.empty((len(words), 2), dtype=object)
    for i, word in enumerate(words):
        scores[i] = [word, validate_word_score(word, words)]
    scores = scores[scores[:, 1].argsort()[::-1]]
    print(scores[:10])

    
main()