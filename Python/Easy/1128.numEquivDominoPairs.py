# 1128. Number of Equivalent Domino Pairs
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/
# Beats: 89.14%
def numEquivDominoPairs(dominoes):
    d = {}
    for dom in dominoes:
        x, y = dom[0], dom[1]
        if x < y:
            temp = (x*10) + y
        else:
            temp = (y*10) + x
        if temp not in d:
            d[temp] = 1
        else:
            d[temp] += 1
    output = []
    for i in d:
        if d[i] > 1:
            n = d[i]
            output.append(int(n*(n-1)/2))
    return sum(output)


dominoes = [[1,2],[2,1],[3,4],[5,6]]
# dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
print(numEquivDominoPairs(dominoes))
