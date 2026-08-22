# 2062. Count Vowel Substrings of a String
# Beats: 8.49%
def countVowelSubstrings(word):
    output = 0
    for i in range(len(word)):
        for j in range(i, len(word)+1):
            if len(word[i:j]) >= 5:
                if set(word[i:j]) == set('aeiouuu'):
                    output += 1
    return output


word = "aeiouu"
word = "unicornarihan"
word = "cuaieuouac"
print(countVowelSubstrings(word))
