"""
write a word count_function ,the function will take file name as input and will print 4 lines of output
 1.number of characters including white spaces,
 2.no of words separated by white spaces,
 3.no of lines in the file,
 4.no of unique words and the unique words are case sensitive --10 points
"""


def word_count(word_count_file):

    file = open('word_count_file.txt', 'r')
    #  print(file.read())
    read_file = file.read()
    num_char_in_file = len(read_file)  # this variable gives the total characters in the file
    num_lines = read_file.split('\n')  # this variable gives the total number of lines in the file
    number_of_words = read_file.split()  # this variable gives the total words in the file

    unique_words = set(number_of_words)  # creating a set in order to get unique words
    if unique_words == set(number_of_words):
        print(f"it contains {len(number_of_words)} number of words separated by white spaces and, \n {len(unique_words)} unique words.")

    print(f'it also contains {num_char_in_file} characters including white spaces.')
    print(f'it also contains {len(num_lines)} lines. \n')


    file.close()

word_count('word_count_file.txt')

name = 'emmanuel mkpurunchi f'
title = 'word count assignment'
print(f'Name: {name.upper()}. \n Title: {title.upper()}.')