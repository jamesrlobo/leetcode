# 3392. Count Subarrays of Length Three With a Condition
# Beats: 23.11%
def countSubarrays(nums):
    count = 0
    for i in range(len(nums)-2):
        temp = nums[i:i+3]
        if temp[0]+temp[2] == temp[1]/2:
            count += 1
    return count


nums = [1,2,1,4,1]
print(countSubarrays(nums))

# def countSubarrays(nums):
#     count = 0
#     for i in range(len(nums)):
#         for j in range(i, len(nums)+1):
#             temp = nums[i:j]
#             if len(temp) == 3 and temp[0]+temp[2] == temp[1]/2:
#                 count += 1
#     return count
