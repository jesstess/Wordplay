import scrabble

# Print all words that are palindromes.
for word in scrabble.wordlist:
    if len(word) > 1 and word == word[::-1]:
        print word
