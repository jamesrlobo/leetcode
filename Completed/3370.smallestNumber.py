# 3370. Smallest Number With All Set Bits
# Beats: 5.03%
def smallestNumber(n):
    l = (len(set(bin(n)[2:])))
    while l != 1:
        n +=1
        l = (len(set(bin(n)[2:])))
    return n


# n = 5
# n = 10
n = 3
print(smallestNumber(n))
