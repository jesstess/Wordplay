import scrabble

VOWELS = ['a', 'e', 'i', 'o', 'u']

# Print all words that have all 5 vowels.
for word in scrabble.wordlist:
    has_all_vowels = True
    for vowel in VOWELS:
        if vowel not in word:
            has_all_vowels = False
            break
    if has_all_vowels:
        print word
