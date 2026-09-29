# 350. Intersection of Two Arrays II
#Beats: 5.07%
def intersect(nums1, nums2):
    output = []
    for i in set(nums1):
        if i in nums2:
            if nums1.count(i) == nums2.count(i):
                for j in range(nums1.count(i)):
                    output.append(i)
            else:
                for j in range(min(nums1.count(i), nums2.count(i))):
                    output.append(i)
    return output

# nums1 = [1,2,2,1]
# nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2))
