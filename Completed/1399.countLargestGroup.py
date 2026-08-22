# 1399. Count Largest Group
# Beats: 5.96%
def countLargestGroup(n):
    count = 0
    d = {}
    for i in range(1, n+1):
        sum = 0
        for j in range(len(str(i))):
            sum += int(str(i)[j])
        if sum not in d:
            d[sum] = [i]
        else:
            d[sum] += [i]
    l = []
    for j in d:
        l.append(len(d[j]))
    m = max(l)
    for k in l:
        if k == m:
            count+=1
    return count


# n = 13
n = 2
print(countLargestGroup(n))
