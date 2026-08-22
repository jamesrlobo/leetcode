# 2958. Length of Longest Subarray With at Most K Frequency
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/
# Beats: 13.17% [Copied from solutions]
def maxSubarrayLength(nums, k):
    n = len(nums)
    ans = 0
    start = -1
    freq = Counter()
    for i in range(n):
        freq[nums[i]] += 1
        while freq[nums[i]] > k:
            start += 1
            freq[nums[start]] -= 1
        ans = max(ans, i-start)
    return ans


nums = [1,2,3,1,2,3,1,2]
k = 2
print(maxSubarrayLength(nums, k))
