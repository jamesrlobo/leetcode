def minIncrementForUnique(nums):
    nums = sorted(nums)
    print(nums)
    count = 0
    for i in range(len(nums)):
        if nums.count(nums[i]) > 1:
            while nums.count(nums[i]) > 1:
                nums[i] += 1
                count += 1
                print(nums)
    return count


nums = [1,2,2]
# nums = [3,2,1,2,1,7]
# nums = [2,2,2,1]
print(minIncrementForUnique(nums))

# def minIncrementForUnique(nums):
#     output = 0
#     if set(nums) == len(nums):
#         return output
#     extra = []
#     for x in set(nums):
#         if nums.count(x) >= 2:
#             for y in range(nums.count(x)-1):
#                 extra.append(x)
#     print(extra)
#     nums = list(set(nums))
#     for i in extra:
#         count = 0
#         while i in nums or i in extra:
#             i = i+1
#             count += 1
#         nums.append(i)
#         output += count
#     return output

# def minIncrementForUnique(nums):
#     count = 0
#     nums = sorted(nums)
#     print(nums)
#     while len(set(nums)) != len(nums):
#         for i in range(len(nums)):
#             if nums.count(nums[i]) > 1:
#                 nums[i] += 1
#                 count += 1
#                 print(nums)
#                 break
#             else:
#                 i+=1
#     return count
