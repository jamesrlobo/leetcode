# 2656. Maximum Sum With Exactly K Elements
# Beats: 47.65%
def maximizeSum(nums, k):
    nums = sorted(nums)
    output = 0
    i = 0
    while i < k:
        output += nums[-1]
        nums[-1] = nums[-1] + 1
        i+=1
    return output


# nums = [1,2,3,4,5]
# k = 3
nums = [5,5,5]
k = 2
print(maximizeSum(nums, k))
