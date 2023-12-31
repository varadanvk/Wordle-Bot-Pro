from algorithm import algorithm
from test import words, read_file
import numpy as np
import random
import string
from concurrent.futures import ThreadPoolExecutor

def main():
    answers = read_file('answers.txt')
    # tested_words = words
    # count=0
    # first_words = []
    
    # with ThreadPoolExecutor() as executor:
    #     for word in tested_words:
    #         scores = np.array([executor.submit(algorithm, answers, answer, word) for answer in answers])
    #         avg_score = np.mean([score.result() for score in scores])
    #         first_words.append([word, avg_score])
    #         count+=1
    #         if count%10==0:
    #             print(f"Word: {word}, Avg Score: {avg_score}")

    # first_words = sorted(first_words, key=lambda x: x[1])
    
    
    
    # # Calculate average score and print top 10 words
    # print('\n-------------------------------------------------------')
    # print(first_words[:50])
    
    # with open('best_words.txt', 'w') as outfile:
    # # Write each capitalized word to the new file
    #     for word in range(50):
    #         outfile.write(first_words[word][0] + ' ' + str(first_words[word][1]) +  '\n')

    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    fails = 0
    for answer in answers:
        if algorithm(answers, answer, 'plats') > 6:
            fails+=1
        elif algorithm(answers, answer, 'plats') ==6:
            sixes+=1
        elif algorithm(answers, answer, 'plats') ==5:
            fives+=1
        elif algorithm(answers, answer, 'plats') ==4:
            fours+=1
        elif algorithm(answers, answer, 'plats') ==3:
            threes+=1
        elif algorithm(answers, answer, 'plats') ==2:
            twos+=1
        elif algorithm(answers, answer, 'plats') ==1:
            ones+=1
    total = ones+twos+threes+fours+fives+sixes+fails
    print("Ones: " , 100*ones/total, "%")
    print("Twos: " , 100*twos/total, "%")
    print("Threes: " , 100*threes/total, "%")
    print("Fours: " , 100*fours/total, "%")
    print("Fives: " , 100*fives/total, "%")
    print("Sixes: " , 100*sixes/total, "%")
    print("Fails: " , 100*fails/total, "%")
    #print(f'Ones: {ones}, Twos: {twos}, Threes: {threes}, Fours: {fours}, Fives: {fives}, Sixes: {sixes}, Fails: {fails}')
    

#['plats', 3.5490506329113924]
main()