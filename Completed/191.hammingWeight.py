# 191. Number of 1 Bits
def hammingWeight(n):
    return str(bin(n))[2:].count('1')


n = 2147483645
print(hammingWeight(n))
