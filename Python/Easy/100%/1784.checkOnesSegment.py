# 1784. Check if Binary String Has at Most One Segment of Ones
# Beats: 100.00%
def checkOnesSegment(s):
    if len(s) <= 2:
        return True
    for i in range(0, len(s)-1, 2):
        if s[i] == s[i+1]:
            return True
    # for i in range(len(s)-1):
    #     if s[i] == s[i+1] and s[i] == "1":
    #         return True
    return False


s = "1001"
s = "110"
s = "1100111"
print(checkOnesSegment(s))
