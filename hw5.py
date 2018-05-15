# -*- coding: utf-8 -*-
from collections import Counter
import csv
import json
import pickle
import string



def main(filename):
    # read file into lines
    lines = open(filename).readlines()
    # declare a word list
    all_words = []
    # extract all words from lines
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]
        # check the format of words and append it to "all_words" list
        words = line.split()
        for word in words:
            # then, remove (strip) unwanted punctuations from every word
            # "dream." => "dream"
            word = word.strip(string.punctuation)
            # check if word is not empty
            if word:
                # append the word to "all_words" list
                all_words.append(word)

    # compute word count from all_words
    counter = Counter(all_words)
    
    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
    with open('wordcount.csv','w') as csv_file:
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(csv_file)
        # write table head
        writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
        writer.writerows(counter.most_common())

    # dump to a json file named "wordcount.json"
   
    json.dump(list(counter.most_common()), open('wordcount.json','w'))
    
    # BONUS: dump to a pickle file named "wordcount.pkl"
    
    pickle.dump(counter , open ('wordcount.pkl','wb'))
    # hint: dump the Counter object directly
    


if __name__ == '__main__':
    main("i_have_a_dream.txt")
