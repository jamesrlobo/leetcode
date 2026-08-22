# 70. Climbing Stairs
# Beats: 100.00%
def climbStairs(n):
    if n == 0 or n == 1:
        return 1
    prev, curr = 1, 1
    for i in range(2, n+1):
        temp = curr
        curr = curr + prev
        prev = temp
    return curr


n = 2
print(climbStairs(n))
