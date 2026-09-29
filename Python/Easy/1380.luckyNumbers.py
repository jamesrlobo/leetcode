# 1380. Lucky Numbers in a Matrix
def luckyNumbers(matrix):
    n = len(matrix)
    col_maximum, row_minimum = [], []
    #find the minimum number in each row
    for i in matrix:
        row_minimum.append(min(i))
    #find the maximum number in each column
    for j in range(len(matrix[0])):
        temp = []
        for k in range(n):
            temp.append(matrix[k][j])
        col_maximum.append(max(temp))
    print(row_minimum, col_maximum)
    res = [item for item in row_minimum if item in col_maximum]
    return res

# matrix = [[3,7,8],[9,11,13],[15,16,17]]
# matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
matrix = [[7,8],[1,2]]
print(luckyNumbers(matrix))
