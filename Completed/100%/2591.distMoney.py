# 2591. Distribute Money to Maximum Children [Copied from solution]
# https://leetcode.com/problems/distribute-money-to-maximum-children/description/
# Beats: 100.00%
def distMoney(money, children):
    moneyleft = money - children
    if moneyleft < 0:
        return -1
    if moneyleft/7 == children and moneyleft%7 == 0:
        return children
    if moneyleft//7 == children-1 and moneyleft%7 == 3:
        return children-2
    else:
        return min(children-1, moneyleft/7)


money = 20
children = 3

# money = 16
# children = 2
#
# money = 5
# children = 2
#
# money = 8
# children = 5
#
# money = 9
# children = 3
print(distMoney(money, children))
