# 2657. Find the Prefix Common Array of Two Arrays
# Beats: 13.96%
def findThePrefixCommonArray(A, B):
    n = len(A)
    output = []
    for i in range(1, n+1):
        # print((A[:i]), (B[:i]))
        output.append(len(set(A[:i]) & set(B[:i])))
    return output


A = [1,3,2,4]
B = [3,1,2,4]

A = [2,3,1]
B = [3,1,2]
print(findThePrefixCommonArray(A, B))
