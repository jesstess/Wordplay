import re
import scrabble

# Use a regular expression to find and print all words containing 'uu'.
pattern = re.compile("uu")
for word in scrabble.wordlist:
    if pattern.search(word):
        print word
