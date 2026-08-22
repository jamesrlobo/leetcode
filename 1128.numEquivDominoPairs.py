# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/
def numEquivDominoPairs(dominoes):
    d = {}
    for i in dominoes:
        print(i)
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d


dominoes = [[1,2],[2,1],[3,4],[5,6]]
dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
print(numEquivDominoPairs(dominoes))
