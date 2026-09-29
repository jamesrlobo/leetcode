#1422. Maximum Score After Splitting a String
# Beats: 49.37%
def maxScore(s):
    score = 0
    for i in range(1, len(s)):
        rhs = s[:i]
        lhs = s[i:]
        temp = rhs.count('0') + lhs.count('1')
        if temp > score:
            score = temp
    return score


s = "011101"
s = "00111"
s = "1111"
print(maxScore(s))
