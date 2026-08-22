# 3083. Existence of a Substring in a String and Its Reverse
# Beats: 100.00%
def isSubstringPresent(s):
    rev_s = s[::-1]
    for i in range(len(s)-1):
        if s[i:i+2] in rev_s:
            return True
    return False


s = "leetcode"
s = "abcba"
s = "abcd"
print(isSubstringPresent(s))
