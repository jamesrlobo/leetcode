# 3678. Smallest Absent Positive Greater Than Average
# Beats: 25.03%
def smallestAbsent(nums):
    average = sum(nums)/len(nums)
    print(average)
    i = min(nums)
    while i <= 100:
        if i > average and i not in nums:
            return i
        i+=1
    return None

# nums = [3,5]
# nums = [-1,1,2]
# nums = [4,-1]
# nums = [-34]
nums = [99]
print(smallestAbsent(nums))
