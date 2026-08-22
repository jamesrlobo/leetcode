# 1081. Smallest Subsequence of Distinct Characters
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description
import itertools
def smallestSubsequence(s):
    dist_chars = len(set(s))
    res = []
    for r in range(len(s)+1):
        for comb in itertools.combinations(s, r):
            res.append("".join(comb))
    return res


s = "bcabc"
s = "cbacdcbc"
s = "cdadabcc"
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(smallestSubsequence(s))

# Memory Limit Exceeded 9 / 68 testcases passed
# def smallestSubsequence(s):
#     dist_chars = len(set(s))
#     output = []
#     res = [""]
#     for char in s:
#         res += [sub + char for sub in res]
#     for i in res:
#         if len(set(i)) == dist_chars and len(i) == dist_chars:
#             output.append(i)
#     output.sort()
#     return output[0]
