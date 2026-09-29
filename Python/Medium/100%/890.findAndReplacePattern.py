# 890. Find and Replace Pattern
# https://leetcode.com/problems/find-and-replace-pattern/description/
# Beats: 100.00%
def findAndReplacePattern(words, pattern):
    output = []
    temp_pattern = ""
    for i in pattern:
        temp_pattern += str(pattern.count(i))
    # print(temp_pattern)
    for word in words:
        temp = ""
        for ch in word:
            temp += str(word.count(ch))
        if temp == temp_pattern:
            d = {}
            for x,y in zip(pattern, word):
                if x not in d:
                    d[x] = y
                else:
                    if d[x] != y:
                        break
            else:
                output.append(word)
    return output


words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abc"
words = ["badc","abab","dddd","dede","yyxx"]
pattern = "baba"
print(findAndReplacePattern(words, pattern))
