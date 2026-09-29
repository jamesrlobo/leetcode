# 2609. Find the Longest Balanced Substring of a Binary String
# Beats: 5.15%
def findTheLongestBalancedSubstring(s):
    output = []
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            temp = s[i:j]
            l = int(len(temp)/2)
            if set(temp[:l]) == {"0"} and set(temp[l:]) == {"1"}:
                output.append(l*2)
    # print(output)
    if output:
        return max(output)
    else:
        return 0


s = "01000111"
s = "00111"
s = "111"
print(findTheLongestBalancedSubstring(s))
