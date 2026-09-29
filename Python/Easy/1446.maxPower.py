#1446. Consecutive Characters
#Beats: 31.08%
def maxPower(s):
    output = [1]
    count = 1
    temp, i = 0, 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            count +=1
            temp = count
        else:
            temp = count
            count = 1
        output.append(temp)
        i+=1
    return max(output)


s = "leetcode"
# s = "abbcccddddeeeeedcba"
# s = "j"
# s = "cc"
print(maxPower(s))
