# 2119. A Number After a Double Reversal
def isSameAfterReversals(num):
    s = str(num)
    reverse1 = int(s[::-1])
    reverse2 = str(reverse1)
    print(num, reverse1, reverse2[::-1])
    return num == int(reverse2[::-1])


# num = 526
num = 1800
print(isSameAfterReversals(num))
