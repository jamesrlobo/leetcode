# 3736. Minimum Moves to Equal Array Elements III
# Beats: 37.53%
def minMoves(nums):
    count = 0
    maximum = max(nums)
    for i in range(len(nums)):
        if nums[i] < maximum:
            count += maximum - nums[i]
    return count


# nums = [2,1,3]
nums = [4,4,5]
print(minMoves(nums))
