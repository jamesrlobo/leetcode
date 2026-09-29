# 2347. Best Poker Hand
# Beats: 100.00%
def bestHand(ranks, suits):
    if len(set(ranks)) == 5 and len(set(suits)) == 1:
        return "Flush"
    for i in ranks:
        if ranks.count(i) >= 3:
            return "Three of a Kind"
    for j in ranks:
        if ranks.count(j) == 2 or ranks.count(j) == 4:
            return "Pair"
    if len(set(ranks)) == 5:
        return "High Card"

# ranks = [3,3,13,7,3]
# suits = ["a","d","d","d","c"]

# ranks = [2,10,7,10,7]
# suits = ["a","b","a","d","b"]

# ranks = [13,2,3,1,9]
# suits = ["a","a","a","a","a"]

ranks = [4,4,2,4,4]
suits = ["d","a","a","b","c"]

# ranks = [10,10,2,12,9]
# suits = ["a","b","c","a","d"]

print(bestHand(ranks, suits))
