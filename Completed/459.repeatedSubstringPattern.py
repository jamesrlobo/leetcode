# 459. Repeated Substring Pattern
def repeatedSubstringPattern(s):
    i = 1
    while i <= len(s)/2:
        if s[:i] * int(len(s)/len(s[:i])) == s:
            return True
        i+=1
    return False


# s = "abab"
# s = "abcabcabcabc"
# s = "ababab"
s = "babbabbabbabbab"
print(repeatedSubstringPattern(s))
