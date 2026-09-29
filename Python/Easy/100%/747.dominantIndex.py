# 747. Largest Number At Least Twice of Others
def dominantIndex(nums):
    maximum = max(nums)
    index = nums.index(maximum)
    nums.sort(reverse=True)
    for i in range(len(nums)):
        if nums[i] != maximum:
            if nums[i]*2 > maximum:
                return -1
    return index

# nums = [3,6,1,0]
# nums = [1,2,3,4]
nums = [0,0,0,1]
print(dominantIndex(nums))
