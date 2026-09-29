# 824. Goat Latin
# https://leetcode.com/problems/goat-latin/description/
# Beats:100.00%
def toGoatLatin(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    sentence = sentence.split(" ")
    # print(sentence)
    n = len(sentence)
    for i in range(n):
        print(sentence[i])
        if sentence[i][0] in vowels:
            sentence[i] = sentence[i]+"ma" + ((i+1)*"a")
        else:
            sentence[i] = sentence[i][1:]+sentence[i][0]+"ma"+((i+1)*"a")
    return " ".join(sentence)


sentence = "I speak Goat Latin"
print(toGoatLatin(sentence))
