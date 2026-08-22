# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/description/
# Beats: 7.70%
def longestPalindrome(s):
    output = ""
    n = len(s)
    for i in range(n):
        for j in range(i, n+1):
            temp = s[i:j]
            if temp == temp[::-1] and temp != "":
                if len(temp) > len(output):
                    output = temp
    return output


s = "babad"
s = "cbbd"
print(longestPalindrome(s))
