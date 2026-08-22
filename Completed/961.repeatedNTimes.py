# 961. N-Repeated Element in Size 2N Array
# Beats: 5.41%
def repeatedNTimes(nums):
    n = len(nums)//2
    for i in set(nums):
        if nums.count(i) == n:
            return i


# nums = [1,2,3,3]
# nums = [2,1,2,5,3,2]
nums = [5,1,5,2,5,3,5,4]
print(repeatedNTimes(nums))
