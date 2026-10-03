# 4065. Rearrange Array by Removing Distinct Values
# https://leetcode.com/problems/rearrange-array-by-removing-distinct-values/description/
#Beats: 94.58%
def rearrangeArray(nums):
    ans = []
    while nums != []:
        to_remove = []
        for i in set(nums):
            to_remove.append(i)
            nums.remove(i)
        ans.extend(sorted(to_remove))
    return ans

# Beats: 44.76%
def rearrangeArray(nums):
    ans = []
    while nums != []:
        to_remove = sorted(list(set(nums)))
        # return to_remove
        ans.extend(to_remove)
        for i in to_remove:
            nums.remove(i)
    return ans


nums = [3,1,3,2,1,3]
nums = [7,7,4,4,4]
nums = [3,9]
print(rearrangeArray(nums))
