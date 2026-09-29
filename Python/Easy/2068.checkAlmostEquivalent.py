# 2068. Check Whether Two Strings are Almost Equivalent
# Beats: 26.81%
def checkAlmostEquivalent(word1, word2):
    for i in set(word1):
        # print("Word1:", word1.count(i))
        # print("Word2:", word2.count(i))
        if (word1.count(i) - word2.count(i)) > 3:
            return False
    for j in set(word2):
        # print("Word1:", word1.count(i))
        # print("Word2:", word2.count(i))
        if (word2.count(j) - word1.count(j)) > 3:
            return False
    return True


word1 = "aaaa"
word2 = "bccb"

word1 = "abcdeef"
word2 = "abaaacc"

word1 = "cccddabba"
word2 = "babababab"

word1 = "zzzyyy"
word2 = "iiiiii"
print(checkAlmostEquivalent(word1, word2))
