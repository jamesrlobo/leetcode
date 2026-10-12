# 4078. Three Fibonacci Sum
# https://leetcode.com/problems/three-fibonacci-sum/description/
# Beats: 100.00%
def threeFibonacciSum(self, n: int) -> bool:
    if n%2 != 0:
        return False
    x = n//2
    a, b = 0, 1
    c = a + b
    while c <= x:
        if a + b + c == n:
            return True
        a = b
        b = c
        c = a + b
        # print(a, b, c)
    return False
