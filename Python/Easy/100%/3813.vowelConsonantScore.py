# 3813. Vowel-Consonant Score
# Beats: 100.00%
import math
def vowelConsonantScore(s):
    score, v, c = 0, 0, 0
    vowels = "aeiou"
    for i in s:
        if i.isalpha():
            if i in vowels:
                v += 1
            else:
                c += 1
    if c != 0:
        return math.floor(v/c)
    else:
        return score


s = "cooear"
s = "axeyizou"
s = "au 123"
s = "i3"
print(vowelConsonantScore(s))
