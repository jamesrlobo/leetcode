# 1817. Finding the Users Active Minutes
# Beats: 25.51%
def findingUsersActiveMinutes(logs, k):
    output = [0] * k
    # print(output)
    d = {}
    for i in range(len(logs)):
        if logs[i][0] not in d:
            d[logs[i][0]] = [logs[i][1]]
        else:
            d[logs[i][0]] += [logs[i][1]]
    # print(d)
    for x in d:
        output[len(set(d[x]))-1] += 1
    return output


logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5

logs = [[1,1],[2,2],[2,3]]
k = 4
print(findingUsersActiveMinutes(logs, k))
