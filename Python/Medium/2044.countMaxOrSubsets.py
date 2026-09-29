# 2044. Count Number of Maximum Bitwise-OR Subsets
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/
# Beats: 24.11%
def countMaxOrSubsets(nums):
    output = {}
    subsets = [[]]
    for num in nums:
        subsets += [i + [num] for i in subsets]
    for subset in subsets:
        if subset != []:
            result = 0
            for x in subset:
                result |= x
            if result not in output:
                output[result] = 1
            else:
                output[result] += 1
    return output[max(output)]


nums = [3,1]
nums = [2,2,2]
nums = [3,2,1,5]
print(countMaxOrSubsets(nums))
