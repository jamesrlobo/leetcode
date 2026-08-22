# 3461. Check If Digits Are Equal in String After Operations I
# Beats: 22.85%
def hasSameDigits(s):
    while len(s) > 2:
        temp = ""
        for i in range(len(s)-1):
            temp += str((int(s[i]) + int(s[i+1]))%10)
        s = temp
    if s[0] == s[1]:
        return True
    return False


s = "3902"
# s = "34789"
print(hasSameDigits(s))
