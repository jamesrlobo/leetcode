# 2293. Min Max Game
# Beats: 100.00%
def minMaxGame(nums):
    if len(nums) == 1:
        return sum(nums)
    while len(nums) > 1:
        temp = []
        count = 0
        for i in range(1, len(nums), 2):
            if count%2 == 0:
                temp.append(min(nums[i-1], nums[i]))
                count += 1
            else:
                temp.append(max(nums[i-1], nums[i]))
                count += 1
        nums = temp
    return sum(nums)


nums = [1,3,5,2,4,8,2,2]
print(minMaxGame(nums))
