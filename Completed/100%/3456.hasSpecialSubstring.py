# 3456. Find Special Substring of Length K
# https://leetcode.com/problems/find-special-substring-of-length-k/description/
# Beats: 100.00%
def hasSpecialSubstring(s, k):
    for i in range(len(s)-k+1):
        print(s[i:i+k])
        output1, output2, output3 = False, False, False
        if len(set(s[i:i+k])) == 1:
            output1 = True
        if i != 0 and s[i] != s[i-1]:
            output2 = True
        elif i == 0:
            output2 = True
        if i+k != len(s) and s[i+k-1] != s[i+k]:
            output3 = True
        elif i+k == len(s):
            output3 = True
        if output1 == output2 and output2 == output3 and output1 == True:
            return True
    return False



s = "aaabaaa"
k = 3
s = "abc"
k = 2
s = "ccc"
k = 2
s = "h"
k = 1
s = "gdgkahhhdf"
k = 2
print(hasSpecialSubstring(s,k))
