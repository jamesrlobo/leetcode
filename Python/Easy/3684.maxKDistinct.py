# 3684. Maximize Sum of At Most K Distinct Elements
# Beats: 64.09%
def maxKDistinct(nums, k):
    nums = sorted(list(set(nums)), reverse=True)
    return nums[:k]


nums = [84,93,100,77,90]
k = 3
# nums = [84,93,100,77,93]
# k = 3
print(maxKDistinct(nums, k))
