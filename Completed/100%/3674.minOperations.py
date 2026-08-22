# 3674. Minimum Operations to Equalize Array
# Beats: 100.00%
def minOperations(nums):
    if len(set(nums)) == 1:
        return 0
    else:
        return 1


nums = [1,2]
print(minOperations(nums))
