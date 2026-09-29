# 2215. Find the Difference of Two Arrays
# https://leetcode.com/problems/find-the-difference-of-two-arrays/
#Beats: 94.70%
def findDifference(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return [list(set1 - set2), list(set2 - set1)]

# def findDifference(nums1, nums2):
#     temp1 = []
#     temp2 = []
#     for i in set(nums1):
#         if i not in nums2:
#             temp1.append(i)
#     for j in set(nums2):
#         if j not in nums1:
#             temp2.append(j)
#     return [temp1, temp2]


# nums1 = [1,2,3]
# nums2 = [2,4,6]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(findDifference(nums1, nums2))


# Beats: 13.38%
# def findDifference(nums1, nums2):
#     answer = []
#     answer.append([x for x in set(nums1) if x not in nums2])
#     answer.append([y for y in set(nums2) if y not in nums1])
#     return answer
