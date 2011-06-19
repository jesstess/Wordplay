import re
from scrabble import wordlist

# Use a regular expression to find and print all words containing 'uu'.
pattern = re.compile("uu")
for word in wordlist:
    if pattern.search(word):
        print word
