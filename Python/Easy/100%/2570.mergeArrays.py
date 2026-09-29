# 2570. Merge Two 2D Arrays by Summing Values
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/
# Beats: 100.00%
def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    d = {}
    output = []
    for i in range(len(nums1)):
        if nums1[i][0] not in d:
            d[nums1[i][0]] = nums1[i][1]
        else:
            d[nums1[i][0]] += nums1[i][1]
    for j in range(len(nums2)):
        if nums2[j][0] not in d:
            d[nums2[j][0]] = nums2[j][1]
        else:
            d[nums2[j][0]] += nums2[j][1]
    for k in d:
        output.append([k, d[k]])
    output.sort(key=lambda x: x[0])
    return output
