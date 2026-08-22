# 3754. Concatenate Non-Zero Digits and Multiply by Sum I
# Beats: 100.00%
def sumAndMultiply(n):
    if n == 0:
        return 0
    x = ""
    sum = 0
    for i in str(n):
        if i in "123456789":
            x += i
            sum += int(i)
    return int(x)*sum


n = 10203004
n = 1000
print(sumAndMultiply(n))
