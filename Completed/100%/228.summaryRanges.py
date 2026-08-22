# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/description/
# Beats: 100.00%
def summaryRanges(nums):
    if nums == []:
        return []
    output = []
    start = 0
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] != 1:
            end = i+1
            temp = nums[start:end]
            if len(temp) > 1:
                output.append(str(temp[0])+"->"+str(temp[-1]))
            else:
                output.append(str(temp[0]))
            start = i+1
    temp = nums[start:]
    if len(temp) > 1:
        output.append(str(temp[0])+"->"+str(temp[-1]))
    else:
        output.append(str(temp[0]))
    return output


nums = [0,1,2,4,5,7] #Expected: ["0->2","4->5","7"]
nums = [0,2,3,4,6,8,9] #Expected: ["0","2->4","6","8->9"]
nums = [-1] #Expected: ["-1"]
nums = [1,2] #Expected: ["1->2"]
nums = []
print(summaryRanges(nums))
