# 3069. Distribute Elements Into Two Arrays I
# Beats: 100.00%
def resultArray(nums):
    arr1, arr2, result = [], [], []
    arr1.append(nums[0])
    arr2.append(nums[1])
    for i in range(2, len(nums)):
        if arr1[-1] > arr2[-1]:
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])
    result = arr1 + arr2
    return result


nums = [2,1,3]
# nums = [5,4,3,8]
print(resultArray(nums))
