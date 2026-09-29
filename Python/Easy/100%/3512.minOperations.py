# 3512. Minimum Operations to Make Array Sum Divisible by K
def minOperations(nums, k):
    return (sum(nums)%k)


# nums = [3,9,7]
# k = 5
nums = [3,2]
k = 6
print(minOperations(nums, k))
