# 2605. Form Smallest Number From Two Digit Arrays
# Beats: 15.31%
def minNumber(nums1, nums2):
    common = list(set(nums1) & set(nums2))
    if common:
        return min(common)
    min1 = min(nums1)
    min2 = min(nums2)
    return min(int(str(min1)+str(min2)), int(str(min2)+str(min1)))


nums1 = [4,1,3]
nums2 = [5,7]
# nums1 = [3,5,2,6]
# nums2 = [3,1,7]
print(minNumber(nums1,nums2))
