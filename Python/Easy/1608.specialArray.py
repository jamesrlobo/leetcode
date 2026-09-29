# 1608. Special Array With X Elements Greater Than or Equal X
#Beats: 46.22%
def specialArray(nums):
    for x in range(1, len(nums)+1):
        count = 0
        for i in nums:
            if i >= x:
                count += 1
        if x == count:
            return x
    return -1


nums = [3,5]
nums = [0,0]
nums = [0,4,3,0,4]
nums = [3,9,7,8,3,8,6,6]
print(specialArray(nums))
