# 2231. Largest Number After Digit Swaps by Parity
# Beats: 100.00%
def largestInteger(num):
    output, even, odd = [], [], []
    for i in str(num):
        if int(i)%2 == 0:
            even.append(int(i))
        else:
            odd.append(int(i))
    even = sorted(even)
    print(even)
    odd = sorted(odd)
    print(odd)
    num = list(str(num))
    for x in range(len(num)):
        if int(num[x])%2 == 0:
            output.append(str(even[-1]))
            even.pop()
        else:
            output.append(str(odd[-1]))
            odd.pop()
    return int("".join(output))


# num = 1234
num = 65875
# num = 247
print(largestInteger(num))
