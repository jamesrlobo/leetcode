# 1967. Number of Strings That Appear as Substrings in Word
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/description/
# Beats: 100.00%
def numOfStrings(patterns, word):
    count = 0
    for pat in patterns:
        if pat in word:
           count += 1
    return count


patterns = ["a","abc","bc","d"]
word = "abc"

patterns = ["a","b","c"]
word = "aaaaabbbbb"

patterns = ["a","a","a"]
word = "ab"
print(numOfStrings(patterns, word))
