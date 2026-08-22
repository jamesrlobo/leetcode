# 3545. Minimum Deletions for At Most K Distinct Characters
# Beats: 100.00%
def minDeletion(s, k):
    count = 0
    print(len(set(s)))
    freq = []
    for i in set(s):
        freq.append(s.count(i))
    freq = sorted(freq)
    print(freq)
    if len(set(s)) == k:
        return 0
    elif len(set(s)) <= k:
        return 0
    else:
        noOfItemToRemove = len(set(s)) - k
        print(noOfItemToRemove)
        for i in range(noOfItemToRemove):
            count += freq[i]
    return count



s = "wyxwmwwjywttt"
k = 1
print(minDeletion(s, k))
