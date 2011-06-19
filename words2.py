from string import ascii_lowercase
from scrabble import wordlist

# Print all letters that never appear doubled in an English word.
for letter in ascii_lowercase:
    exists = False
    for word in wordlist:
        if letter * 2 in word:
            exists = True
            break
    if not exists:
        print "There are no English words with a double " + letter
