# 3954. Sum of Compatible Numbers in Range I
# https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/description/
# Beats: 100.00%
def sumOfGoodIntegers(n, k):
    output = 0
    for x in range(1, n+k+1):
        if abs(n-x) <= k and (n & x) == 0:
            output += x
    return output


n = 2
k = 3
print(sumOfGoodIntegers(n,k))
