def wiggleSort(nums):
    nums = sorted(nums)
    n = len(nums)
    for i in range(0, (n//2)+1, 2):
        temp = nums.pop()
        nums.insert(i+1,temp)
    return nums


nums = [1,5,1,1,6,4]
nums = [1,3,2,2,3,1]
# nums = [1,1,2,1,2,2,1]
print(wiggleSort(nums))
