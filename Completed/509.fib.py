# 509. Fibonacci Number
# Beats: 52.10%
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev = 0
    prev_1  = 1
    for i in range(1, n):
        ans = prev + prev_1
        prev_1 = prev
        prev = ans
    return ans


n = 2
print(fib(n))
