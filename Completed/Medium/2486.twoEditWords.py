# 2452. Words Within Two Edits of Dictionary
# https://leetcode.com/problems/words-within-two-edits-of-dictionary/description/
# Beats: 35.54%
def twoEditWords(queries, dictionary):
    output = []
    for i in queries:
        for j in dictionary:
            diff = 0
            for ch in range(len(i)):
                if i[ch] != j[ch]:
                    diff += 1
            if diff <= 2:
                output.append(i)
                break
    return output


queries = ["word","note","ants","wood"]
dictionary = ["wood","joke","moat"]
# queries = ["yes"]
# dictionary = ["not"]
print(twoEditWords(queries, dictionary))
