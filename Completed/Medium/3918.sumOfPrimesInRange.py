# 3918. Sum of Primes Between Number and Its Reverse
# https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/description/
# Beats: 76.66%
import math

def is_prime(i):
    if i <= 1:
        return False
    if i == 2:
        return True
    if i%2 == 0:
        return False
    for j in range(3, int(math.sqrt(i))+1, 2):
        if i%j == 0:
            return False
    return True

def sumOfPrimesInRange(n):
    total = 0
    m = int(str(n)[::-1])
    print(m)
    if n < m:
        low = n
        high = m
    else:
        high = n
        low = m
    for i in range(low, high+1):
        if is_prime(i):
            total += i
    return total


n = 13
print(sumOfPrimesInRange(n))
