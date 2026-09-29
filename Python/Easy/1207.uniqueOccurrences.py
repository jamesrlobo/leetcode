# 1207. Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/description/
# Beats: 25.64%
def uniqueOccurrences(arr):
    occurrences = []
    for i in set(arr):
        if arr.count(i) not in occurrences:
            occurrences.append(arr.count(i))
        else:
            return False
    return True


arr = [1,2,2,1,1,3]
arr = [1,2]
arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(uniqueOccurrences(arr))
