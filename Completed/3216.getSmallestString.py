# 3216. Lexicographically Smallest String After a Swap
# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/description/
# Beats: 5.43%
def getSmallestString(s):
    n = len(s)
    if n == 1:
        return s
    output = {int(s):s}
    for i in range(n-1):
        int_s = [x for x in s]
        if int(int_s[i])%2 == int(int_s[i+1])%2:
            temp = int_s[i]
            int_s[i] = int_s[i+1]
            int_s[i+1] = temp
        output[int("".join(int_s))] = "".join(int_s)
    final = min(output)
    return output[final]


s = "45320"
s = "001"
s = "10"
s = "13"
print(getSmallestString(s))
