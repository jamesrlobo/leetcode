# 2540. Minimum Common Value
# Beats: 14.63%
def getCommon(nums1, nums2):
    common = list(set(nums1) & set(nums2))
    if len(common) > 0:
        return min(common)
    else:
        return -1


nums1 = [1,2,3]
nums2 = [2,4]

# nums1 = [1,2,3,6]
# nums2 = [2,3,4,5]
print(getCommon(nums1, nums2))
