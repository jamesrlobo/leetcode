# 1893. Check if All the Integers in a Range Are Covered
# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/
# Beats: 100.00%
def isCovered(ranges, left, right):
    to_check = []
    for i in range(left, right+1):
        to_check.append(i)
    print(to_check)
    temp = []
    for item in ranges:
        temp += [x for x in range(item[0], item[1]+1)]
    print(temp)
    for j in to_check:
        if j not in temp:
            return False
    return True

ranges = [[1,2],[3,4],[5,6]]
left = 2
right = 5

ranges = [[1,10],[10,20]]
left = 21
right = 21
print(isCovered(ranges, left, right))
