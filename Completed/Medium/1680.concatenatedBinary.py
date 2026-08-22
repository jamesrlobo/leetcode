# 1680. Concatenation of Consecutive Binary Numbers
# Beats: 18.24%
def concatenatedBinary(n):
    output = ""
    mod = 10**9 + 7
    for i in range(1, n+1):
        output += bin(int(i))[2:]
    return (int(output, 2))%mod


n = 1
n = 3
n = 12
print(concatenatedBinary(n))
