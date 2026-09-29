# 1342. Number of Steps to Reduce a Number to Zero
# Beats: 100.00%
def numberOfSteps(num):
    steps = 0
    while num != 0:
        if num%2 == 0:
            num = num//2
            steps += 1
        else:
            num = num-1
            steps += 1
    return steps


num = 14
num = 8
num = 123
print(numberOfSteps(num))
