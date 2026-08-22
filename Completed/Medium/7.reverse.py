# 7. Reverse Integer
# Beats: 77.79%
def reverse(x):
    output = 0
    if str(x)[0] == "-":
        temp = "-"
        x = str(x)[1:]
        output = int(temp+x[::-1])
    else:
        output = int(str(x)[::-1])
    if output< -2147483648 or output > 2147483647:
        return 0
    else:
        return output


x = 123
x = -123
print(reverse(x))
