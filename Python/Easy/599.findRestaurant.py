# 599. Minimum Index Sum of Two Lists
# Beats: 37.28%
def findRestaurant(list1, list2):
    common = list(set(list1) & set(list2))
    index = []
    d = {}
    if len(common) == 0:
        return 0
    for i in common:
        min_index = list1.index(i) + list2.index(i)
        index.append(min_index)
        if min_index not in d:
            d[min_index] = [i]
        else:
            d[min_index] += [i]
    output = min(index)
    return d[output]


list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
print(findRestaurant(list1, list2))
