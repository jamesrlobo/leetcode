# 2269. Find the K-Beauty of a Number
# Beats: 100.00%
def divisorSubstrings(num, k):
    output = 0
    string = str(num)
    n = len(string)
    for i in range(n-k+1):
        if int(string[i:i+k]) != 0 and num%int(string[i:i+k]) == 0:
            output+=1
    return output


num = 240
k = 2

num = 430043
k = 2
print(divisorSubstrings(num, k))
