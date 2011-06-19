import re
from scrabble import wordlist

# Use a regular expression to find an print all words matching certain character
# constraints.
pattern = re.compile("^e.g....r$")
for word in wordlist:
    if pattern.search(word):
        print word
