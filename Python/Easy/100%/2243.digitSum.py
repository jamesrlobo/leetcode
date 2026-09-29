# 2243. Calculate Digit Sum of a String
# Beats: 100.00%
def digitSum(s,k):
    while len(s) > k:
        i = 0
        new_s = ""
        while i < len(s):
            temp = 0
            for j in range(len(s[i:i+k])):
                temp += int(s[i:i+k][j])
            i+=k
            new_s += str(temp)
        s = new_s
    return s

# s = "11111222223"
# k = 3
# s = "00000000"
# k = 3
s = "11"
k = 2
print(digitSum(s,k))
