# 867. Transpose Matrix
def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        new_matrix.append(temp)
    return new_matrix


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3],[4,5,6]]
print(transpose(matrix))
