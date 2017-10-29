import os
import re
import string
from statistics import mean

in_filepath = os.path.join('raw_data','paragraph_2.txt')

with open(in_filepath, 'r') as text:
    lines = text.read()

    ##PARAGRAPHS: Split text into paragraphs, then remove empty strings
    para_split = [s.strip() for s in lines.splitlines()] #Creates list of paragraphs
    while '' in para_split: para_split.remove('') #removes emtpy strings from list

    ##PARAGRAPHS: Paragraph count & sentences per paragraph
    para_count = len(para_split)
    para_sent = [re.split('\. |\? |! |;', x) for x in para_split]
    para_sent_count = [len(sent) for sent in para_sent]
    para_sent_mean = float(round(mean(para_sent_count), 1))

    ##PARAGRAPHS: Words per paragraph
    para_word_count = [len(para.split()) for para in para_split]
    para_word_mean = float(round(mean(para_word_count), 1))
    
    ##SENTENCES: Total sentences
    total_sent = sum(para_sent_count)

    ##SENTENCES: Words per sentence and average sentence length
    sent_list = [item for sublist in para_sent for item in sublist] #creates single list of sentences
    sent_word_count = [len(sent.split()) for sent in sent_list]
    sent_word_mean = float(round(mean(sent_word_count), 1))

    ##WORDS: Total words
    total_word = sum(sent_word_count)
    
    ##WORDS: Average word length
    word_clean = " ".join(word.strip(string.punctuation) for word in lines.split()) #removes all punctuation and joins all words as single string with spaces between each word
    word_list = word_clean.split() #Creates list of words from cleaned word string
    word_char_count = [len(char) for char in word_list]
    word_char_mean = float(round(mean(word_char_count), 1))


    ##PRINT: Analysis
    print("-------------------------------------")
    print("TEXT ANALYSIS")
    print("-------------------------------------")
    print(f"Total word count: {total_word}")
    print(f"Total sentence count: {total_sent}")
    print(f"Total paragraph count: {para_count}\n")
    print(f"Average characters per word: {word_char_mean}")
    print(f"Average words per sentence: {sent_word_mean}")
    print(f"Average sentences per paragraph: {para_sent_mean}")
    print(f"Average words per paragraph: {para_word_mean}")
    print("-------------------------------------")

    #---------------------------------#
    out_filesave = input("Do you want to save results to text file? (y)es or (n)o: ")
    if out_filesave == "y":
        out_filename = input("Please enter a filename to save as: ")
        out_filename = "Output/" + out_filename + ".txt"
        fh = open(out_filename,'w')
        fh.write("TEXT ANALYSIS\n")
        fh.write("-------------------------------\n")
        fh.write(f"Total word count: {total_word}\n")
        fh.write(f"Total sentence count: {total_sent}\n")
        fh.write(f"Average characters per word: {word_char_mean}\n")
        fh.write(f"Average words per sentence: {sent_word_mean}\n")
        fh.write(f"Average sentences per paragraph: {para_sent_mean}\n")
        fh.write(f"Average words per paragraph: {para_word_mean}\n")
        fh.write("-------------------------------------")
        fh.close()