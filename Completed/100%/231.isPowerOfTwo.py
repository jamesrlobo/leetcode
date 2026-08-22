# 231. Power of Two
# Beats: 100.00%
def isPowerOfTwo(self, n: int) -> bool:
    if n < 0:
        return False
    n = (bin(abs(n))[2:]).count('1')
    if n == 1:
        return True
    else:
        return False
