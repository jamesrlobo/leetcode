# 3663. Find The Least Frequent Digit
# Beats: 48.61%
def getLeastFrequentDigit(n):
    d = {}
    string = str(n)
    for i in set(string):
        if string.count(i) not in d:
            d[string.count(i)] = [i]
        else:
            d[string.count(i)] += [i]
    output = min(d)
    return min(d[output])


n = 1553322
# n = 723344511
print(getLeastFrequentDigit(n))
