# 3852. Smallest Pair With Different Frequencies
# Beats: 5.10%
def minDistinctFreqPair(nums):
    output = []
    for i in set(nums):
        for j in set(nums):
            if i < j and nums.count(i) != nums.count(j):
                output.append([i, j])
    if len(output) > 0:
        return min(output)
    return [-1,-1]


nums = [1,1,2,2,3,4]
# nums = [1,5]
# nums = [7]
print(minDistinctFreqPair(nums))
