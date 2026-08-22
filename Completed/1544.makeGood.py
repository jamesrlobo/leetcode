# 1544. Make The String Great
# Beats: 46.81%
def makeGood(s):
    s = list(s)
    i = 1
    while i < len(s):
        print(s)
        if ord(s[i-1]) == ord(s[i]):
            i += 1
        elif ord(s[i-1]) == ord(s[i])+32:
            print(s[i-1], ord(s[i-1]), s[i], ord(s[i])+32)
            s.pop(i)
            s.pop(i-1)
            i = 1
        elif ord(s[i-1]) == ord(s[i])-32:
            print(s[i-1], ord(s[i-1]), s[i], ord(s[i])-32)
            s.pop(i)
            s.pop(i-1)
            i = 1
        else:
            i+=1
    return "".join(s)


s = "leEeetcode"
s = "abBAcC"
s = "s"
print(makeGood(s))
