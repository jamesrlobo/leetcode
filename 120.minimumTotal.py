def minimumTotal(triangle):
    output = list(triangle[0])
    n = len(triangle)
    ind = 0
    for i in range(1, n):
        if triangle[i][ind] > triangle[i][ind+1]:
            output.append(triangle[i][ind+1])
            ind = ind+1
        else:
            output.append(triangle[i][ind])
    print(output)
    return sum(output)


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]
triangle = [[-1],[2,3],[1,-1,-3]]
triangle = [[-1],[3,2],[-3,1,-1]]
print(minimumTotal(triangle))

# def minimumTotal(triangle):
#     output = list(triangle[0])
#     n = len(triangle)
#     ind = 0
#     for i in range(1, n):
#         if triangle[i][ind] > triangle[i][ind+1]:
#             output.append(triangle[i][ind+1])
#             ind = ind+1
#         else:
#             output.append(triangle[i][ind])
#     print(output)
#     return sum(output)
