# 190. Reverse Bits
def reverseBits(n):
    return (int(format(n, '032b')[::-1], 2))

# n = 43261596
n = 2147483644
print(reverseBits(n))
