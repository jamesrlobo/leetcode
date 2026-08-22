# 2210. Count Hills and Valleys in an Array
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/
# Beats: 100.00%
def countHillValley(nums):
    new_nums = []
    n = len(nums)
    count = 0
    for i in range(1, n):
        if nums[i-1] != nums[i]:
            new_nums.append(nums[i-1])
    new_nums.append(nums[n-1])
    m = len(new_nums)
    for j in range(1, m-1):
        if new_nums[j-1] >= new_nums[j] and new_nums[j] < new_nums[j+1]:
            count += 1
        elif new_nums[j-1] < new_nums[j] and new_nums[j] > new_nums[j+1]:
            count+= 1
    return count


nums = [2,4,1,1,6,5]
nums = [6,6,5,5,4,1]
print(countHillValley(nums))
