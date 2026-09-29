# 3871. Count Commas in Range II
# https://leetcode.com/problems/count-commas-in-range-ii/description/
# Beats: 100.00% [Copied from editorial]
def countCommas(n):
    p = 1000
    res = 0
    while p <= n:
        res += n - p + 1
        p = 1000 * 1000
    return res


n = 1002
print(countCommas(n))
