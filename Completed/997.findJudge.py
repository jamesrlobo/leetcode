# 997. Find the Town Judge [Copied from solutions]
# https://leetcode.com/pro blems/find-the-town-judge/description/
# Beats : 31.03%
def findJudge(n, trust):
    trust_list = [[0,0] for x in range(n+1)]
    # print(trust_list)
    for i in trust:
        trust_list[i[0]][0] += 1
        trust_list[i[1]][1] += 1
    # print(trust_list)
    for j in range(1, len(trust_list)):
        if trust_list[j][0] == 0 and trust_list[j][1] == n-1:
            return j
    return -1


n = 2
trust = [[1,2]]

n = 3
trust = [[1,3],[2,3]]

n = 3
trust = [[1,3],[2,3],[3,1]]
print(findJudge(n, trust))
