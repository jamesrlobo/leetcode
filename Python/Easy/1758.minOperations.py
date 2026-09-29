# 1758. Minimum Changes To Make Alternating Binary String
# Beats: 5.58%
def minOperations(s):
    s1 = [x for x in s]
    s2 = [x for x in s]
    count = []
    count1 = 0
    for i in range(len(s)):
        if i%2 == 0 and s1[i] != '1':
            s1[i] = '1'
            count1 += 1
        elif i%2 == 1 and s1[i] != '0':
            s1[i] = '0'
            count1 += 1
    count.append(count1)
    count2 = 0
    for j in range(len(s)):
        if j%2 == 0 and s2[j] != '0':
            s1[j] = '0'
            count2 += 1
        elif j%2 == 1 and s2[j] != '1':
            s2[j] = '0'
            count2 += 1
    count.append(count2)
    return min(count)


s = "0100"
s = "10"
s = "1111"
s = "10010100"
print(minOperations(s))
