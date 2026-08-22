# 2169. Count Operations to Obtain Zero
# Beats: 63.60%
def countOperations(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    if num1 == num2:
        return 1
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 < num2:
            num2 -= num1
        else:
            num1 -= num2
        count += 1
    return count


num1 = 2
num2 = 3
num1 = 0
num2 = 0
print(countOperations(num1, num2))
