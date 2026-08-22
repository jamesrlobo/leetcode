# 3870. Count Commas in Range
# Beats: 100.00%
def countCommas(n):
    output = (n+1) - 1000
    if output >= 0:
        return output
    else:
        return 0


n = 1002
n = 998
print(countCommas(n))
