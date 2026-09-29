# 3861. Minimum Capacity Box
# Beats: 100.00%
def minimumIndex(capacity, itemSize):
    output = []
    for i in range(len(capacity)):
        if capacity[i] >= itemSize:
            output.append(capacity[i])
    if len(output) == 0:
        return -1
    output = sorted(output)
    print(output)
    return capacity.index(output[0])


capacity = [1,5,3,7]
itemSize = 3

capacity = [3,5,4,3]
itemSize = 2

capacity = [4]
itemSize = 5
print(minimumIndex(capacity, itemSize))
