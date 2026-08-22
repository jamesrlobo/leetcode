# 1805. Number of Different Integers in a String
# https://leetcode.com/problems/number-of-different-integers-in-a-string/description/
# Beats: 100.00%
def numDifferentIntegers(word):
    new_word, output = [], []
    s = ""
    for i in range(len(word)):
        if word[i].isdigit():
            s += word[i]
        else:
            if len(s) and s not in new_word:
                new_word.append(s)
            s = ""
    if len(s) and s not in new_word:
        new_word.append(s)
    for number in new_word:
        if int(number) not in output:
            output.append(int(number))
    if output:
        return len(output)
    else:
        return 0


word = "a123bc34d8ef034"
word = "leet1234code234"
word = "a1b01c001"
print(numDifferentIntegers(word))
