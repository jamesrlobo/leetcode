# 2545. Sort the Students by Their Kth Score
# Beats: 100.00%
def sortTheStudents(score, k):
    output, order = [], []
    for i in range(len(score)):
        order.append((score[i][k], i))
    order =  sorted(order, reverse=True)
    for x in range(len(order)):
        output.append(score[order[x][1]])
    return output


# score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
# k = 2
score = [[3,4],[5,6]]
k = 0
print(sortTheStudents(score, k))
