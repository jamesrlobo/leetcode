# 3898. Find the Degree of Each Vertex
# https://leetcode.com/problems/find-the-degree-of-each-vertex/description/
# Beats: 100.00%
def findDegrees(matrix):
    n = len(matrix)
    output = []
    for i in range(n):
        output.append(sum(matrix[i]))
    return output


# matrix = [[0,1,1],[1,0,1],[1,1,0]]
# matrix = [[0,1,0],[1,0,0],[0,0,0]]
print(findDegrees(matrix))
