# 3364. Minimum Positive Sum Subarray
# Beats: 5.00%
def minimumSumSubarray(nums, l, r):
    output = []
    i = 0
    while i < len(nums):
        for j in range(l, r+1):
            n = len(nums[i:i+j])
            if n >= l and n <= r:
                if sum(nums[i:i+j]) > 0:
                    print(nums[i:i+j])
                    output.append(sum(nums[i:i+j]))
        i+=1
    # print(output)
    if len(output) > 0:
        return min(output)
    return -1


nums = [3, -2, 1, 4]
l = 2
r = 3

nums = [-2, 2, -3, 1]
l = 2
r = 3

nums = [1, 2, 3, 4]
l = 2
r = 4
print(minimumSumSubarray(nums, l, r))

# def minimumSumSubarray(nums, l, r):
#     output = []
#     for i in range(len(nums)):
#         for j in range(i, len(nums)+1):
#             if len(nums[i:j]) >= l and len(nums[i:j]) <= r and sum(nums[i:j]) > 0:
#                 output.append(sum(nums[i:j]))
#     if len(output) > 0:
#         return min(output)
#     return -1
