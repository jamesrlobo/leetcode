# 2942. Find Words Containing Character
# https://leetcode.com/problems/find-words-containing-character/
# Beats: 100.00%
def findWordsContaining(words, x):
    n = len(words)
    output = []
    for i in range(n):
        if x in words[i]:
            output.append(i)
    return output


words = ["leet","code"]
x = "e"
print(findWordsContaining(words,x))
