import csv
from test import words
data = list(csv.reader(open('unigram_freq.csv')))

frequency_list = []

for index in range(len(data)):
    if(len(data[index][0]) == 5) and (data[index][0] in words):
        frequency_list.append([data[index][0], data[index][1]])

print(len(frequency_list))
frequency_list = sorted(frequency_list, key=lambda x: x[1], reverse=True)

def frequency(word):
    if word in frequency_list:
        return frequency_list[word]
    else:
        return 1
    
    
with open('frequency.txt', 'w') as outfile:
    for index in range(len(frequency_list)):
        outfile.write(frequency_list[index][0] + ' ' + str(len(frequency_list)-index) + '\n')
