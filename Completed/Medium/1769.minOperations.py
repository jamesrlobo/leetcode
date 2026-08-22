# 1769. Minimum Number of Operations to Move All Balls to Each Box
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
# Beats: 5.02%
def minOperations(boxes):
    output = []
    n = len(boxes)
    for i in range(n):
        count = 0
        for j in range(n):
            if i != j:
                count += int(boxes[j]) * abs(i-j)
        output.append(count)
    return output


boxes = "110"
boxes = "001011"
print(minOperations(boxes))
