# 2244. Minimum Rounds to Complete All Tasks
# Beats: 85.12%
from collections import Counter
def minimumRounds(tasks):
    count = 0
    cntr = Counter(tasks)
    print(cntr)
    for j in cntr:
        if cntr[j] < 2:
            return -1
        while cntr[j] >= 3:
            count += cntr[j]//3
            cntr[j] = cntr[j]%3
        if cntr[j] >0:
            count += 1
    return count


# tasks = [2,2,3,3,2,4,4,4,4,4]
# tasks = [2,3,3]
tasks = [69,65,62,64,70,68,69,67,60,65,69,62,65,65,61,66,68,61,65,63,60,66,68,66,67,65,63,65,70,69,70,62,68,70,60,68,65,61,64,65,63,62,62,62,67,62,62,61,66,69]
print(minimumRounds(tasks))


# def minimumRounds(tasks):
#     count = 0
#     d = {}
#     for i in set(tasks):
#         if tasks.count(i) <= 1:
#             return -1
#         else:
#             d[i] = tasks.count(i)
#     for j in d:
#         while d[j] >= 3:
#             count += d[j]//3
#             d[j] = d[j]%3
#         if d[j] >0:
#             count += 1
#     return count

#====================

# def minimumRounds(tasks):
#     count = 0
#     for i in set(tasks):
#         if tasks.count(i) <= 1:
#             return -1
#         else:
#             temp = tasks.count(i)
#             while temp >= 3:
#                 count += temp//3
#                 temp = temp%3
#             if temp > 0:
#                 count += 1
#     return count
