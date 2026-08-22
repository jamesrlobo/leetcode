# 1572. Matrix Diagonal Sum
def diagonalSum(mat):
    primary_diagonal, secondary_diagonal = [], []
    n = len(mat[0])
    for i in range(n):
        primary_diagonal.append(mat[i][i])

    for j in range(n):
        secondary_diagonal.append(mat[j][(n-1)-j])
    if n%2 == 0:
        return sum(primary_diagonal) + sum(secondary_diagonal)
    else:
        return (sum(primary_diagonal) + sum(secondary_diagonal)) - primary_diagonal[n//2]


mat = [[1,2,3],[4,5,6],[7,8,9]]
# mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
print(diagonalSum(mat))
