# 3330. Find the Original Typed String I
# https://leetcode.com/problems/find-the-original-typed-string-i/description/
# Beats: 73.14%
def possibleStringCount(word):
    output = 1
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            output += 1
    return output


word = "abbcccc"
word = "abcd"
word = "aaaa"
print(possibleStringCount(word))
