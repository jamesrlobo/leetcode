# 3658. GCD of Odd and Even Sums
# Beats: 100.00%
import math


def gcdOfOddEvenSums(n):
    a = n*n #sumOdd
    b = n * (n+1) #sumEven
    return math.gcd(a,b)

# n = 4
# n = 5
# n = 1
print(gcdOfOddEvenSums(n))
