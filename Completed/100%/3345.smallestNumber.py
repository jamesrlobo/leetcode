# 3345. Smallest Divisible Digit Product I
# Beats: 100.00%
def smallestNumber(n, t):
    prod = 1
    for i in str(n):
        prod *= int(i)
    while prod%t != 0:
        n += 1
        prod = 1
        for j in str(n):
            prod *= int(j)
    return n

n = 10
t = 2

n = 15
t = 3

n = 16
t = 4
print(smallestNumber(n, t))
