# 2148. Count Elements With Strictly Smaller and Greater Elements
def countElements(nums):
    if len(set(nums)) < 3:
        return 0
    return len(nums) - nums.count(min(nums)) - nums.count(max(nums))


# nums = [11,7,2,15]
# nums = [-3,3,3,90]
nums = [11, 12, 1,1,1,1,1,1,2,2,2,2,3,3]
print(countElements(nums))
