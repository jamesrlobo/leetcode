def residuePrefixes(s):
    residue = []
    l = len(s)
    for i in range(1, l+1):
        if len(set(s[:i])) == (len(s[:i])%3):
            residue.append(len(set(s[:i])))
    return len(residue)


s = "abc"
s = "dd"
s = "bob"
s = "kl"
print(residuePrefixes(s))
