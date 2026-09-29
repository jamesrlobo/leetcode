1282. Group the People Given the Group Size They Belong To
Beats: 100.00%
def groupThePeople(groupSizes):
    output = []
    d = {}
    for i in range(len(groupSizes)):
        if groupSizes[i] not in d:
            d[groupSizes[i]] = [i]
        else:
            d[groupSizes[i]] += [i]
    for x in d:
        temp = []
        for j in range(len(d[x])):
            temp.append(d[x][j])
            if len(temp) == x:
                output.append(temp)
                temp = []
        if temp:
            output.append(temp)
    return output


# groupSizes = [3,3,3,3,3,1,3]
groupSizes = [2,1,3,3,3,2]
print(groupThePeople(groupSizes))
