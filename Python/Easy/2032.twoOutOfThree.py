# 2032. Two Out of Three
# Beats: 65.99%
def twoOutOfThree(nums1,nums2,nums3):
    first = list(set(nums1) & set(nums2))
    second = list(set(nums2) & set(nums3))
    third = list(set(nums3) & set(nums1))
    output = list(set(first+second+third))
    return output


# nums1 = [1,1,3,2]
# nums2 = [2,3]
# nums3 = [3]

# nums1 = [3,1]
# nums2 = [2,3]
# nums3 = [1,2]

nums1 = [1,2,2]
nums2 = [4,3,3]
nums3 = [5]
print(twoOutOfThree(nums1,nums2,nums3))
