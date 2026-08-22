def isPowerOfThree(n):
    if n <= 0:
        return False
    while n%3 == 0:
        n = n//3
        print(n)
    if n == 1:
        return True
    else:
        return False


n = 27
# n = 0
# n = -1
# n = 45
print(isPowerOfThree(n))
