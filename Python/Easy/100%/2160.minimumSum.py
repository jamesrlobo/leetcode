# 2160. Minimum Sum of Four Digit Number After Splitting Digits
def minimumSum(num):
    num = list(str(num))
    num.sort()
    num1 = int(num[0] + num[2])
    num2 = int(num[1] + num[3])
    return (num1 + num2)


# num = 2932
num = 4009
print(minimumSum(num))
