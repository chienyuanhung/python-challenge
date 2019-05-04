import os
import csv
import re

#create the path for the text file

txt_file = 'paragraph_1.txt'
data_path= os.path.join('raw_data',txt_file)

#read the text file

with open(data_path) as data_file:
    textreader = data_file.read()

#counts sentences number
text = re.split("(?<=[.!?]) +", textreader)   

total_sentence = len(text) 

#word count and letter count

word_count = 0
letter_counts = 0
for sentence in text:
    word_count += len(sentence.split(' '))
    new_sentence = sentence.split(' ')
    for word in new_sentence:
        letter_counts += len(word)    

#average letter counts and average sentence length
ave_letter_count = round((letter_counts/word_count), 1)
ave_sentence_len = round((word_count/total_sentence), 1)


print('Paragraph Analysis')
print('-----------------')
print(f'Approximate Word Count: {word_count}')
print(f'Approximate Sentence Count: {total_sentence}')
print(f'Average Letter Count: {ave_letter_count}')
print(f'Average Sentence Length: {ave_sentence_len}')
    