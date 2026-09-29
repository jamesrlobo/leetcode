# 2566. Maximum Difference by Remapping a Digit
# Beats: 100.00%
def minMaxDifference(num):
    num = [x for x in str(num)]
    length = len(num)
    i, j, maxToReplace, minToReplace = 0, 0, 0, 0
    while i < length:
        if num[i] in "876543210":
            maxToReplace = num[i]
            break
        i+=1
    while j < length:
        if num[j] in "987654321":
            minToReplace = num[j]
            break
        i+=1
    num1, num2 = [], []
    num1.extend(num)
    num2.extend(num)
    for item1 in range(length):
        if num1[item1] == maxToReplace:
            num1[item1] = '9'
    for item2 in range(length):
        if num2[item2] == minToReplace:
            num2[item2] = '0'
    return int("".join(num1)) - int("".join(num2))


num = 11891
num = 90
print(minMaxDifference(num))
