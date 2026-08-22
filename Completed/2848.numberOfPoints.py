# 2848. Points That Intersect With Cars
# Beats: 5.65%
def numberOfPoints(nums):
    output = []
    for i in nums:
        for j in range(i[0], i[1]+1):
            if j not in output:
                output.append(j)
    return len(output)


# nums = [[1,3],[5,8]]
nums = [[3,6],[1,5],[4,7]]
print(numberOfPoints(nums))
