# 3876. Construct Uniform Parity Array II
# https://leetcode.com/problems/construct-uniform-parity-array-ii/description/
# Beats: 57.93%
def uniformArray(nums1):
    n = len(nums1)
    nums1 = sorted(nums1)
    mn = min(nums1)
    if mn%2 != 0:
        return True
    for i in range(1, n):
        if nums1[i]%2 != 0:
            return False
    return True


nums1 = [1,4,7]
nums1 = [2,3]
print(uniformArray(nums1))
