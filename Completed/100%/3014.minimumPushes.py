# 3014. Minimum Number of Pushes to Type Word I
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/
# Beats: 100.00%
def minimumPushes(word):
    n = len(word)
    if n <= 8:
        return n
    n -= 8
    count = 8
    i = 2
    while n > 0:
        if n > 8:
            n -= 8
            count += (8 * i)
            i+= 1
        else:
            count += (n * i)
            n = 0
            i+=1
    return count


word = "abcde"
word = "xycdefghij"
# word = "abcdefghij"
print(minimumPushes(word))
