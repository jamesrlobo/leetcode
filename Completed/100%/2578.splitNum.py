# 2578. Split With Minimum Sum
# Beats: 100.00%
def splitNum(num):
    num = str(num)
    nums = []
    for i in range(len(str(num))):
        nums.append(int(num[i]))
    nums = sorted(nums)
    i = 0
    nums1, nums2 = "", ""
    while i < len(nums):
        if i%2 == 0:
            nums1 += str(nums[i])
        else:
            nums2 += str(nums[i])
        i+=1
    return int(nums1) + int(nums2)

num = 4325
num = 687
print(splitNum(num))
