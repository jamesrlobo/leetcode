# 506. Relative Ranks
def findRelativeRanks(score):
    print(score)
    sorted_score = sorted(score, reverse=True)
    print(sorted_score)
    if len(score) == 1:
        return ["Gold Medal"]
    elif len(score) == 2:
        gold = sorted_score[0]
        silver = sorted_score[1]
        for j in range(len(score)):
            if score[i] == gold:
                res.append("Gold Medal")
            elif score[i] == silver:
                res.append("Silver Medal")
    else:
        gold = sorted_score[0]
        silver = sorted_score[1]
        bronze = sorted_score[2]
        res = []
        for i in range(len(score)):
            if score[i] == gold:
                res.append("Gold Medal")
            elif score[i] == silver:
                res.append("Silver Medal")
            elif score[i] == bronze:
                res.append("Bronze Medal")
            else:
                res.append(str(sorted_score.index(score[i])+1))
    return res


# score = [5,4,3,2,1]
# score = [10,3,8,9,4]
score = [123123,11921,1,0,123]
print(findRelativeRanks(score))
