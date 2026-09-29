# 2091. Removing Minimum and Maximum From Array
# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/description/
# Beats: 46.53%
def minimumDeletions(nums):
    if len(nums) == 1:
        return 1
    n = len(nums)
    output = []
    min_index = nums.index(min(nums))
    max_index = nums.index(max(nums))
    # print(len(nums[:max(min_index, max_index)]))
    output.append(len(nums[:max(min_index, max_index)])+1)
    # print(len(nums[min(min_index, max_index):]))
    output.append(len(nums[min(min_index, max_index):]))
    if min_index < max_index:
        print("here:", (nums[:min_index+1]), (nums[max_index:]))
        print(len(nums[:min_index+1])+len(nums[max_index:]))
        output.append(len(nums[:min_index+1])+len(nums[max_index:]))
    else:
        print("There:", (nums[:max_index+1]), (nums[min_index:]))
        print(len(nums[:max_index+1])+len(nums[min_index:]))
        output.append(len(nums[:max_index+1])+len(nums[min_index:]))
    print(output)
    return min(output)


nums = [2,10,7,5,4,1,8,6]
nums = [0,-4,19,1,8,-2,-3,5]
nums = [101]
nums = [-14,61,29,-18,59,13,-67,-16,55,-57,7,74]
nums = [-87,60,-30,-67,74,55,76,-53]
print(minimumDeletions(nums))
