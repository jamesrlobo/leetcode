# 1534. Count Good Triplets
#Beats: 12.57%
def countGoodTriplets(arr, a, b, c):
    output = []
    l = len(arr)
    for i in range(l):
        for j in range(i, l):
            for k in range(j, l):
                if i < j < k < l:
                    if (abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                        output.append([arr[i], arr[j], arr[k]])
    return len(output)


arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3

# arr = [1,1,2,2,3]
# a = 0
# b = 0
# c = 1
print(countGoodTriplets(arr, a, b, c))
