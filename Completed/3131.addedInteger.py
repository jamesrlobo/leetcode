# 3131. Find the Integer Added to Array I
def addedInteger(nums1, nums2):
    nums1.sort()
    nums2.sort()
    for i, j in zip(nums1, nums2):
        output = j - i
    return output


# nums1 = [2,6,4]
# nums2 = [9,7,5]
# nums1 = [10]
# nums2 = [5]
nums1 = [1,1,1,1]
nums2 = [1,1,1,1]
print(addedInteger(nums1, nums2))
