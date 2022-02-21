#!/usr/bin/python3
words = ['now this is podracing', 'chuba', 'bantha poodoo', 'eat my exhaust', 'sleemo','nucha na bota']
letters = ['b', 'e']

def print_upper_words(word_list):
    """accepts a word list, prints upper-cased version of each word in list"""
    for word in word_list:
        print(word.upper())

print_upper_words(words)

def print_e_words(word_list):
    """accepts a word list, prints words that start with the letter E"""
    for word in word_list:
        if word.startswith('e') or word.startswith('E'):
            print(word)

print_e_words(words)



def print_upper_starts_with(word_list, letters_list):
    """accepts a list of words and a list of letters; if the word begins with a letter from the list of letters, it returns the word uppercased"""
    for word in word_list:
        for letter in letters_list:
            if word.lower().startswith(letter.lower()):
                print(word.upper())

print_upper_starts_with(words, letters)
# For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!

# Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

# Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

# Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

# For example:

# # this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                    must_start_with={"h", "y"})