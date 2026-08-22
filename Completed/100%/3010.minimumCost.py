# 3010. Divide an Array Into Subarrays With Minimum Cost I
# Beats: 100.00%
def minimumCost(nums):
    output = nums[0] + sorted(nums[1:])[0] + sorted(nums[1:])[1]
    return output


nums = [1,2,3,12]
nums = [5,4,3]
nums = [10,3,1,1]
print(minimumCost(nums))
