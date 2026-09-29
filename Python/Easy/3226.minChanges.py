# 3226. Number of Bit Changes to Make Two Integers Equal
# Beats: 12.98%
def minChanges(n,k):
    n = list(bin(n)[2:])
    k = list(bin(k)[2:])
    count = 0
    if n == k:
        return 0
    while len(k) > len(n):
        n.insert(0,'0')
    while len(n) > len(k):
        k.insert(0,'0')
    print(n,k)
    for i in range(len(n)):
        if (n[i]) == '1' and k[i] == '0':
            n[i] = '0'
            count +=1
    print(n,k)
    if n == k:
        return count
    else:
        return -1


n = 13
k = 4
# n = 21
# k = 21
# n = 14
# k = 13
print(minChanges(n,k))
