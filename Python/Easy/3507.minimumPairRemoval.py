# 3507. Minimum Pair Removal to Sort Array I
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/
# Beats: 38.46%
def minimumPairRemoval(nums):
    n = len(nums)
    count = 0
    if n == 1:
        return count
    while nums != sorted(nums):
        temp = []
        for i in range(n-1):
            temp.append(nums[i]+nums[i+1])
            # print(temp)
        target = temp.index(min(temp))
        nums[target] = min(temp)
        nums.pop(target+1)
        count += 1
        n = len(nums)
        # print(nums)
    return count


nums = [5,2,3,1]
nums = [1,2,2]
nums = [2,2,-1,3,-2,2,1,1,1,0,-1]
nums = [-2,1,2,-1,-1,-2,-2,-1,-1,1,1]
print(minimumPairRemoval(nums))
