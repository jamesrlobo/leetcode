# 3774. Absolute Difference Between Maximum and Minimum K Elements
# Beats: 100%
def absDifference(nums, k):
    high, low = 0, 0
    increasing_order = sorted(nums)
    decreasing_order = sorted(nums, reverse=True)
    for i in range(k):
        high += increasing_order[i]
        low += decreasing_order[i]
    return abs(high-low)


nums = [5,2,2,4]
k = 2

nums = [100]
k = 1
print(absDifference(nums, k))
