# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/description/
# Beats: 5.01%
def countSubstrings(s):
    output = []
    n = len(s)
    for i in range(n):
        for j in range(i, n+1):
            temp = s[i:j]
            if temp == temp[::-1] and temp != "":
                output.append(temp)
    print(output)
    return len(output)


s = "abc"
s = "aaa"
print(countSubstrings(s))
