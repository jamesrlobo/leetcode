# 3114. Latest Time You Can Obtain After Replacing Characters
# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/description/
# Beats: 45.50%
def findLatestTime(s):
    if s == "??:??" or s == "12:59":
        return "11:59"
    s = s.split(":")
    print(s)
    #convert hour
    if s[0] == "??":
        s[0] = "11"
    if s[0][0] == "?":
        if int(s[0][1]) >= 2:
            s[0] = "0" + str(s[0][1])
        else:
            s[0] = "1" + str(s[0][1])
    if s[0][1] == "?":
        if s[0][0] == "0":
            s[0] = s[0][0] + "9"
        else:
            s[0] = s[0][0] + "1"
    #convert minute
    if s[1] == "??":
        s[1] = "59"
    if s[1][0] == "?":
        s[1] = "5" + str(s[1][1])
    if s[1][1] == "?":
        s[1] = s[1][0] + "9"
    return ":".join(s)


# s = "1?:?4"
# s = "0?:5?"
# s = "?3:12"
# s = "??:??"
# s = "?2:2?"
s = "12:59"
print(findLatestTime(s))
