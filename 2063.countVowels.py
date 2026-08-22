# 2063. Vowels of All Substrings
# https://leetcode.com/problems/vowels-of-all-substrings/description/
def countVowels(word):
    count = 0
    for i in range(len(word)):
        for j in range(i, len(word)+1):
            if len(word[i:j]) > 0:
                for ch in (word[i:j]):
                    if ch in "aeiou":
                        count += 1
    return count


word = "aba"
word = "abc"
word = "ltcd"
print(countVowels(word))
