# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/description/
# Beats: 85.91% [Copied from solutions]
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n - 1
        ans = n
        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
