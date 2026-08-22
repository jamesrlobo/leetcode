# 1828. Queries on Number of Points Inside a Circle
# Beats: 27.82%
import math
def countPoints(points, queries):
    output = []
    for circle in queries:
        x1 = circle[0]
        y1 = circle[1]
        radius = circle[2]
        temp = 0
        for point in points:
            x2 = point[0]
            y2 = point[1]
            euclideanDistance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            if euclideanDistance <= radius:
                temp += 1
        output.append(temp)
    return output


points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]

points = [[1,1],[2,2],[3,3],[4,4],[5,5]]
queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
print(countPoints(points, queries))
