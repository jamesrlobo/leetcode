# 2788. Split Strings by Separator
# https://leetcode.com/problems/split-strings-by-separator/description/
# Beats: 82.99%
def splitWordsBySeparator(words):
    result = []
    for word in words:
        temp = word.split(separator)
        for i in temp:
            if i != "":
                result.append(i)
    return result


words = ["one.two.three","four.five","six"]
separator = "."

words = ["$easy$","$problem$"]
separator = "$"
print(splitWordsBySeparator(words))
