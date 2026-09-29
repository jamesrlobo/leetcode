# 914. X of a Kind in a Deck of Cards
# Beats: 5.02%
def hasGroupsSizeX(deck):
    if deck == [1]:
        return False
    d = []
    for i in set(deck):
        d.append(deck.count(i))
    print(d)
    for j in range(2, max(set(d))+1):
        print(j)
        for k in set(d):
            if k%j != 0:
                break
        else:
            return True
    return False


deck = [1,2,3,4,4,3,2,1]
# deck = [1,1,1,2,2,2,3,3]
# deck = [0,0,0,1,1,1,2,2,2,2,2,2]
# deck = [1]
# deck = [1,1,1,1,2,2,2,2,2,2]
print(hasGroupsSizeX(deck))
