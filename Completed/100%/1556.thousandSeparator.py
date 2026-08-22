# 1556. Thousand Separator
def thousandSeparator(n):
    res = []
    n = list(str(n)[::-1])
    i = 0
    while i < len(n):
        if i%3 == 0:
            res.append(".")
            res.append(n[i])
        else:
            res.append(n[i])
        i+=1
    if res[0] == ".":
        res.pop(0)
    return ("".join(res))[::-1]


n = 1234
# n = 987
print(thousandSeparator(n))
