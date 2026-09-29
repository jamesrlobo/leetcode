# 1137. N-th Tribonacci Number
# Beats: 100.00%
def tribonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    sum = 0
    one = 0
    two = 1
    three = 1
    for i in range(2, n):
        sum = one + two + three
        one = two
        two = three
        three = sum
    return sum


n = 4
print(tribonacci(n))
