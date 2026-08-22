# 1791. Find Center of Star Graph
def findCenter(edges):
    output = edges[0]
    for i in edges[1:]:
        for j in output:
            if j not in i:
                output.remove(j)
                return output.pop()


edges = [[1,2],[5,1],[1,3],[1,4]]
print(findCenter(edges))
