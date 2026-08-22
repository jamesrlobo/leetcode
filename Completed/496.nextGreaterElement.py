# 496. Next Greater Element I
# Beats: 5.00%
def nextGreaterElement(nums1, nums2):
    output = []
    for i in range(len(nums1)):
        print(nums1[i])
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                for k in nums2[j:]:
                    if k > nums1[i]:
                        output.append(k)
                        break
                else:
                    output.append(-1)
    return output


nums1 = [4,1,2]
nums2 = [1,3,4,2]

nums1 = [2,4]
nums2 = [1,2,3,4]

nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]
print(nextGreaterElement(nums1, nums2))
