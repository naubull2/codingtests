"""
Given a pattern and a string, find if string follows the same pattern.
Here follow means a full matching pattern.
Finding a match between char in pattern to a non-empty word in a string
ex.
 pattern "aab" - string "dog dog cat" => True
"""
def wordPattern(pattern, sentence):
    words = sentence.split()
    # Edge case of pattern mismatch by length
    if len(words) != len(pattern):
        return False

    char2word = dict()
    for i, c in enumerate(pattern):
        w = words[i]
        if c in char2word:
            if char2word[c] != w:
                return False
            else:
                continue
        elif w in list(char2word.values()):
            return False
        # either a new match or an existing one
        char2word[c] = w

    return True


pat="abaabbc"
words="dog cat dog dog cat cat donkey"
print(wordPattern(pat, words))
