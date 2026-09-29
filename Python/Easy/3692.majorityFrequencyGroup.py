# 3692. Majority Frequency Characters
# Beats: 44.55%
def majorityFrequencyGroup(s):
    freq = {}
    for ch in set(s):
        if s.count(ch) not in freq:
            freq[s.count(ch)] = ch
        else:
            freq[s.count(ch)] += ch
    print(freq)
    distinctCharacters = max(freq)
    for i in freq:
        if len(freq[i]) > len(freq[distinctCharacters]):
            distinctCharacters = i
    higherFrequency = distinctCharacters
    for j in freq:
        if j!=higherFrequency and len(freq[j]) == len(freq[higherFrequency]):
            print(freq[j], j, freq[higherFrequency], higherFrequency)
            if j > higherFrequency:
                higherFrequency = j
    return freq[higherFrequency]


# s = "aaabbbccdddde"
# s = "abcd"
s = "pfpfgi"
# s = "adnphaoxnu"
# s = "lxihmlmdri"
# s = "aomwgwfjgahxxqwjfalulctytyitpxmdcmbqbljlkszmdddfoc"
print(majorityFrequencyGroup(s))
