# 1984. Minimum Difference Between Highest and Lowest of K Scores
# Beats: 5.10%
def minimumDifference(nums, k):
    if len(nums) < 2:
        return 0
    output = []
    nums = sorted(nums)
    print(nums)
    for i in range(len(nums)):
        print(nums[i:i+k], max(nums[i:i+k]), min(nums[i:i+k]))
        if len(nums[i:i+k]) == k:
            output.append(max(nums[i:i+k]) - min(nums[i:i+k]))
    return min(output)


nums = [90]
k = 1

nums = [9,4,1,7]
k = 2

nums = [87063,61094,44530,21297,95857,93551,9918]
k = 6
print(minimumDifference(nums, k))
