# 231. Power of Two
# Beats: 4.98%
def isPowerOfTwo(n):
    if n < 0:
        return False
    n = (bin(abs(n))[2:]).count('1')
    if n == 1:
        return True
    else:
        return False


n = 3
print(isPowerOfTwo(n))
