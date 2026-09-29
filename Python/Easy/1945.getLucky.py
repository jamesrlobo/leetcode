# 1945. Sum of Digits of String After Convert
# Beats: 65.26%
def getLucky(s, k):
    string  = ""
    for i in range(len(s)):
        string += str(ord(s[i])-96)
    # print(string)
    while k > 0:
        output = 0
        k -= 1
        for x in string:
            output += int(x)
        string = str(output)
    return string



s = "leetcode"
k = 2
# s = "iiii"
# k = 1
print(getLucky(s, k))
