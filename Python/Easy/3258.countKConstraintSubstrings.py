# 3258. Count Substrings That Satisfy K-Constraint I
# Beats: 21.72%
def countKConstraintSubstrings(s, k):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            temp = s[i:j]
            if temp.count('0') <= k or temp.count('1') <= k:
                count +=1
    return count


s = "10101"
k = 1
s = "1010101"
k = 2
s = "11111"
k = 1
print(countKConstraintSubstrings(s, k))
