# 448. Find All Numbers Disappeared in an Array
#Beats: 81.77%
def findDisappearedNumbers(nums):
    set_nums = set(nums)
    n = len(nums)
    output = []
    for i in range(1, n+1):
        if i not in set_nums:
            output.append(i)
    return output


# nums = [4,3,2,7,8,2,3,1]
# nums = [1,1]
nums = [2,2]
print(findDisappearedNumbers(nums))
