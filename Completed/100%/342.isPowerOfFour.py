# 342. Power of Four
# Beats: 100.00%
def isPowerOfFour(n):
    if n == 1:
        return True
    if n < 4:
        return False
    bit_n = bin(n)[2:]
    print(bit_n)
    if bit_n[0] != '1':
        return False
    for i in range(1, len(bit_n)):
        if bit_n[i] != '0' or bit_n.count('0')%2 != 0:
            return False
    return True


n = 8
print(isPowerOfFour(n))
