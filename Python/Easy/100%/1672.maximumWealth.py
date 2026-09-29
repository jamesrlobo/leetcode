# 1672. Richest Customer Wealth
# Beats:100.00%
def maximumWealth(accounts):
    wealth = [sum(x) for x in accounts]
    return max(wealth)


accounts = [[1,2,3],[3,2,1]]
print(maximumWealth(accounts))
