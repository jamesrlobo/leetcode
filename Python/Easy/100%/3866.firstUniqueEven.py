# 3866. First Unique Even Element
# Beats: 100.00%
def firstUniqueEven(nums):
    for i in nums:
        if nums.count(i) == 1 and i%2 == 0:
            return i
    return -1


nums = [3,4,2,5,4,6]
nums = [4,4]
nums = [6,10]
print(firstUniqueEven(nums))
