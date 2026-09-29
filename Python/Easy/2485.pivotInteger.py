# 2485. Find the Pivot Integer
# Beats: 16.87%
def pivotInteger(n):
    if n == 1:
        return 1
    nums = [x for x in range(1, n+1)]
    print(nums)
    for i in range(len(nums)):
        print(nums[:i], nums[i-1:])
        if sum(nums[:i]) == sum(nums[i-1:]):
            return nums[i-1]
    return -1


n = 1
print(pivotInteger(n))
