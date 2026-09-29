# 693. Binary Number with Alternating Bits
# Beats: 100.00%
def hasAlternatingBits(n):
    n = bin(n)[2:]
    print(n)
    for i in range(len(n)-1):
        print(n[i], n[i+1])
        if n[i] == '1' and n[i+1] != '0':
            return False
        elif n[i] == '0' and n[i+1] != '1':
            return False
    return True


n = 4
print(hasAlternatingBits(n))
