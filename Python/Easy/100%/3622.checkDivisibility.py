# 3622. Check Divisibility by Digit Sum and Product
# Beats: 100.00%
def checkDivisibility(n):
    sum, product = 0, 1
    for i in str(n):
        sum += int(i)
        product *= int(i)
    if n%(sum+product) == 0:
        return True
    else:
        return False


n = 99
n = 23
n = 10
print(checkDivisibility(n))
