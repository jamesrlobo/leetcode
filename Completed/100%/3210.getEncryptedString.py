# 3210. Find the Encrypted String
# https://leetcode.com/problems/find-the-encrypted-string/description/
# Beats :100.00%
def getEncryptedString(s,k):
    result = ""
    n = len(s)
    for i in range(n):
        result += s[(i+k)%n]
    return result


# s = "dart"
# k = 3
s = "aaa"
k = 1
print(getEncryptedString(s,k))
