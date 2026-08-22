# 1337. The K Weakest Rows in a Matrix
def kWeakestRows(mat):
    output, res = [], []
    for i in range(len(mat)):
        res.append([mat[i].count(1), i])
    sorted_res = sorted(res, key=lambda x: x[0])
    for j in range(k):
        output.append(sorted_res[j][1])
    return output


# mat =[[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
# k = 3
mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
k = 2
print(kWeakestRows(mat))
