# 1636. Sort Array by Increasing Frequency
#Refer: https://www.geeksforgeeks.org/python/python-custom-sorting-in-list-of-tuples/
from operator import itemgetter


def frequencySort(nums):
    output = []
    d = []
    for i in set(nums):
        d.append([i, nums.count(i)])
    d.sort(key=itemgetter(0), reverse=True)
    d.sort(key=itemgetter(1))
    for i in d:
        for j in range(i[1]):
            output.append(i[0])
    return output


# nums = [1,1,2,2,2,3]
# nums = [2,3,1,3,2]
nums = [-1,1,-6,4,5,-6,1,4,1]
print(frequencySort(nums))
