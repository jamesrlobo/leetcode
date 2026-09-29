# 2287. Rearrange Characters to Make Target String
# https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/
# Beats: 100.00%
def rearrangeCharacters(s, target):
    x, y = {}, {}
    output = []
    for i in set(target):
        x[i] = s.count(i)
        y[i] = target.count(i)
    for letter in set(target):
        # print(x[letter], y[letter])
        output.append(x[letter]//y[letter])
    return min(output)


s = "ilovecodingonleetcode"
target = "code"

s = "abcba"
target = "abc"

s = "abbaccaddaeea"
target = "aaaaa"

s = "hshac"
target = "h"
print(rearrangeCharacters(s, target))
