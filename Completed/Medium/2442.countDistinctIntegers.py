# 2442. Count Number of Distinct Integers After Reverse Operations
# Beats: 97.05%
def countDistinctIntegers(nums):
    for i in range(len(nums)):
        nums.append(int(str(nums[i])[::-1]))
    return len(set(nums))


nums = [1,13,10,12,31]
nums = [2,2,2]
print(countDistinctIntegers(nums))
