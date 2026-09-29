# 2465. Number of Distinct Averages
# Beats: 4.36%
def distinctAverages(nums):
    nums = sorted(nums)
    avg = []
    while len(nums) != 0:
        avg += [(min(nums) + max(nums)) / 2]
        nums.remove(min(nums))
        nums.remove(max(nums))
    return len(set(avg))


nums = [4,1,4,0,3,5]
nums = [1,100]
print(distinctAverages(nums))
