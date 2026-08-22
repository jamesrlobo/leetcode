3438. Find Valid Pair of Adjacent Digits in String
Beats: 25.57%
def findValidPair(s):
    output = ""
    for i in range(len(s)-1):
        print(s[i], s.count(s[i]), s[i+1], s.count(s[i+1]))
        if s[i] != s[i+1] and int(s[i]) == s.count(s[i]) and int(s[i+1]) == s.count(s[i+1]):
            output = s[i]+s[i+1]
            return output
    return output


# s = "2523533"
# s = "221"
# s = "22"
s = "9212"
print(findValidPair(s))
