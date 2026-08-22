# 2133. Check if Every Row and Column Contains All Numbers
def checkValid(matrix):
    n = len(matrix[0])
    vertical_row = []
    acceptable_items = [x for x in range(1, n+1)]
    for i in matrix:
        # print(set(i))
        if set(i) != set(acceptable_items):
            return False
    for i in range(n):
        for j in range(n):
            vertical_row.append(matrix[j][i])
            if len(vertical_row) == n:
                if set(vertical_row) != set(acceptable_items):
                    return False
                else:
                    vertical_row = []
    return True


matrix = [[1,2,3],[3,1,2],[2,3,1]]
# matrix = [[1,1,1],[1,2,3],[1,2,3]]
# matrix = [[1,2,3],[2,1,3],[3,2,1]]
print(checkValid(matrix))
