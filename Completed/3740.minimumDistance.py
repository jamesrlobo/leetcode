# 3740. Minimum Distance Between Three Equal Elements I
# Beats: 5.28%
def minimumDistance(nums):
    if len(nums) < 3:
        return -1
    output = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if i != j != k and nums[i] == nums[j] == nums[k]:
                    output.append(abs(i - j) + abs(j - k) + abs(k - i))
    if output:
        return min(output)
    else:
        return -1


nums = [1,2,1,1,3]
nums = [1,1,2,3,2,1,2,1]
# nums = [1]
print(minimumDistance(nums))
