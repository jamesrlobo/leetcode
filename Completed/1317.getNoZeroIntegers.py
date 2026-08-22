# 1317. Convert Integer to the Sum of Two No-Zero Integers
def getNoZeroIntegers(n):
    if n == 2:
        return [1, 1]
    for i in range(1, n, 1):
        print(i)
        for j in range(n, 1, -1):
            print(i, j)
            if i + j == n:
                if '0' not in str(i) and '0' not in str(j):
                    return [i,j]



n = 2
print(getNoZeroIntegers(n))
