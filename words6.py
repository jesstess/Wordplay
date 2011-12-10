import re
import scrabble

# Use a regular expression to find an print all words matching certain character
# constraints.
pattern = re.compile("^e.g....r$")
for word in scrabble.wordlist:
    if pattern.search(word):
        print word
