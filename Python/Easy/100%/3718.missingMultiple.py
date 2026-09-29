# 3718. Smallest Missing Multiple of K
# Beats: 100.00%
def missingMultiple(nums, k):
    for i in range(1, 100):
        if i%k == 0 and i not in nums:
            return i


# nums = [8,2,3,4,6]
# k = 2
nums = [1,4,7,10,15]
k = 5
print(missingMultiple(nums, k))
