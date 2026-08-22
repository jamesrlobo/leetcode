# 1827. Minimum Operations to Make the Array Increasing
# Beats: 15.12%
def minOperations(nums):
    count = 0
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums[i+1] += 1
            count += 1
        elif nums[i] > nums[i+1]:
            temp = (nums[i] - nums[i+1] + 1)
            nums[i+1] += temp
            count += temp
        i+=1
    return count


# nums = [1,1,1]
# nums = [1,5,2,4,1]
nums = [8]
print(minOperations(nums))
