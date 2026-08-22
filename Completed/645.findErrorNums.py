# 645. Set Mismatch (Copied from solutions)
# Beats: 89.31%
def findErrorNums(nums):
    n = len(nums)
    actual_sum = (n * (n+1))//2
    array_sum = 0
    unique_sum = 0
    s = set()
    for a in nums:
        array_sum += a

    for a in nums:
        s.add(a)

    for a in s:
        unique_sum += a

    missing = actual_sum - unique_sum
    duplicate = array_sum - unique_sum
    return [duplicate, missing]



nums = [1,2,2,4]
# nums = [1,1]
# nums = [2,2]
# nums = [3,2,2]
print(findErrorNums(nums))
