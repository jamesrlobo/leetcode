def countCompleteSubarrays(nums):
    d = {}
    n = len(nums)
    count = 0
    dist_nums = len(set(nums))
    for i in range(n):
        for j in range(i, n+1):
            print(nums[i:j])
            if len(nums[i:j]) >= dist_nums:
                if len(set(nums[i:j])) == dist_nums:
                    count += 1
            elif len(set(nums[i:j])) > dist_nums:
                break
    return count


nums = [1,3,1,2,2]
nums = [5,5,5,5]
print(countCompleteSubarrays(nums))

# def countCompleteSubarrays(nums):
#     dist = len(set(nums))
#     i, count = 0, 0
#     n = len(nums)
#     while i <= n:
#         j = i + dist
#         while j <= n:
#             temp = (nums[i:j])
#             if len(set(temp)) < dist:
#                 j += 1
#             elif len(set(temp)) == dist:
#                 count+=1
#                 j += 1
#             else:
#                 break
#         i+=1
#     return count
