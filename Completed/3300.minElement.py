# 3300. Minimum Element After Replacement With Digit Sum
def minElement(nums):
    new  = []
    for i in nums:
        sum = 0
        for j in str(i):
            sum += int(j)
        new.append(sum)
    return min(new)


nums = [10,12,13,14]
# nums = [1,2,3,4]
# nums = [999,19,199]
print(minElement(nums))
