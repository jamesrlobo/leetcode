# 3432. Count Partitions with Even Sum Difference
# Beats: 26.81%
def countPartitions(nums):
    count = 0
    for i in range(1, len(nums)):
        if (sum(nums[:i]) - sum(nums[i:])) %2 == 0:
            count += 1
    return count


nums = [10,10,3,7,6]
nums = [1,2,2]
nums = [2,4,6,8]
print(countPartitions(nums))
