# 3396. Minimum Number of Operations to Make Elements in Array Distinct
# Beats: 100.00%
def minimumOperations(nums):
    output = 0
    if nums == []:
        return output
    while len(set(nums)) != len(nums):
        nums = nums[3:]
        output += 1
    return output


nums = [1,2,3,4,2,3,3,5,7]
nums = [4,5,6,4,4]
print(minimumOperations(nums))
