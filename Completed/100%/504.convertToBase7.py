# 504. Base 7
# Beats: 100.00%
def convertToBase7(num):
    if num == 0:
        return "0"
    n = abs(num)
    digits = [x for x in range(7)]
    output = ""
    while n > 0:
        rem = n%7
        output = str(digits[rem]) + output
        n //= 7
    if num < 0:
        output = "-" + output
    return output


# num = 100
# num = -7
num = 0
print(convertToBase7(num))
