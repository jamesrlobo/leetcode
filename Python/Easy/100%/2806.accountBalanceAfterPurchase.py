# 2806. Account Balance After Rounded Purchase
# Beats: 100.00%
from math import floor


def accountBalanceAfterPurchase(purchaseAmount):
    return 100 - floor((purchaseAmount + 5)/10)*10


purchaseAmount = 9
purchaseAmount = 15
purchaseAmount = 10
print(accountBalanceAfterPurchase(purchaseAmount))
