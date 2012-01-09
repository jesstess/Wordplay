import scrabble

VOWELS = ['a', 'e', 'i', 'o', 'u']

def has_all_vowels(word):
    for vowel in VOWELS:
        if vowel not in word:
            return False
    return True

# Print all words that have all 5 vowels.
for word in scrabble.wordlist:
    if has_all_vowels(word):
        print word
