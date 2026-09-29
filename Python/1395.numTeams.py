# https://leetcode.com/problems/count-number-of-teams/
# 1395. Count Number of Teams
def numTeams(rating):
    output = 0
    n = len(rating)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1  , n):
                if rating[i] < rating[j] and rating[j] < rating[k]:
                    output += 1
                elif rating[i] > rating[j] and rating[j] > rating[k]:
                    output += 1
    return output


rating = [2,5,3,4,1]
rating = [2,1,3]
rating = [1,2,3,4]
print(numTeams(rating))
