# 1869. Longer Contiguous Segments of Ones than Zeros
# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/description/
# Beats: 100.00%
def checkZeroOnes(s):
    n = len(s)
    count = 0
    length_one = []
    for i in range(n):
        if s[i] == "1":
            count += 1
        else:
            if count > 0:
                length_one.append(count)
                count = 0
    length_one.append(count)
    count = 0
    length_zero = []
    for j in range(n):
        if s[j] == "0":
            count += 1
        else:
            if count > 0:
                length_zero.append(count)
                count = 0
    length_zero.append(count)
    print(length_one, length_zero)
    if max(length_zero) < max(length_one):
        return True
    return False


s = "1101"
s = "111000"
s = "110100010"
s = "011000111"
print(checkZeroOnes(s))
