# 1910. Remove All Occurrences of a Substring
# Beats: 6.72%
def removeOccurrences(s, part):
    l = len(part)
    stack = []
    i = 0
    while part in s:
        if s[i:i+l] == part:
            s = s[:i] + s[i+l:]
            i = -1
        else:
            i += 1

    return s


s = "daabcbaabcbc"
part = "abc"

s = "axxxxyyyyb"
part = "xy"
print(removeOccurrences(s, part))
