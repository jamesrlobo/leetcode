# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Beats: 81.58% [Copied from solutions]
def findDuplicates(nums):
    seen = set()
    output = []
    for i in nums:
        if i in seen:
            output.append(i)
        else:
            seen.add(i)
    return output


nums = [4,3,2,7,8,2,3,1]
nums = [2,5,2,1,1,4]
print(findDuplicates(nums))
