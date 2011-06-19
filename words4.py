from scrabble import wordlist

# Print all words that are palindromes.
for word in wordlist:
    if len(word) > 1 and word == word[::-1]:
        print word
