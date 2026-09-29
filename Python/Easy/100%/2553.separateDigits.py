# 2553. Separate the Digits in an Array
# https://leetcode.com/problems/separate-the-digits-in-an-array/description/
# Beats: 100.00%
def separateDigits(nums):
    output = []
    n = len(nums)
    for i in range(n):
        temp = str(nums[i])
        for j in range(len(temp)):
            output.append(int(temp[j]))
    return output


nums = [13,25,83,77]
print(separateDigits(nums))
