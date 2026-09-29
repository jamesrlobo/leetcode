# 2357. Make Array Zero by Subtracting Equal Amounts
# Beats: 100.00%
def minimumOperations(nums):
    if 0 not in nums:
        return len(set(nums))
    else:
        return len(set(nums))-1


# nums = [1,5,0,3,5]
nums = [0]
print(minimumOperations(nums))
