# 2389. Longest Subsequence With Limited Sum
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/
# Beats: 22.91%
def answerQueries(nums, queries):
    output = []
    nums  = sorted(nums)
    # print(nums)
    for query in queries:
        print("To comapre:", query)
        temp = []
        for i in range(len(nums)):
            temp.append(nums[i])
            if sum(temp) > query:
                output.append(len(temp)-1)
                temp = []
                break
    if temp:
        # print(temp)
        output.append(len(temp))
    return output
