# 4043. Count Rotations With Exactly K Equal Adjacent Pairs
# https://leetcode.com/problems/count-rotations-with-exactly-k-equal-adjacent-pairs/description/
# Beats: 22.53%
def countRotations(s, k):
    n = len(s)
    output = 0
    for i in range(n):
        temp = (s[i:] + s[:i])
        count = 0
        for i in range(1, n):
            if temp[i-1] == temp[i]:
                count += 1
        if count == k:
            output += 1
    return output


s = "aab"
k = 1
print(countRotations(s,k))
