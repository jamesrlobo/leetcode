# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/
def numEquivDominoPairs(dominoes):
    d = {}
    for i in range(len(dominoes)):
        temp = tuple(dominoes[i])
        if temp not in d and temp[::-1] not in d:
            d[temp] = 1
            for j in range(i, len(dominoes)):
                if i < j:
                    if temp == tuple(dominoes[j]):
                        d[temp] += 1
                    elif temp == tuple(dominoes[j][::-1]):
                        d[temp] += 1
    print(d)
    n = max(d.values())
    return (n*(n-1))//2


dominoes = [[1,2],[2,1],[3,4],[5,6]]
# dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
print(numEquivDominoPairs(dominoes))
