# 884. Uncommon Words from Two Sentences
# Beats: 100.00%
def uncommonFromSentences(s1, s2):
    output = []
    list1 = s1.split(" ")
    list2 = s2.split(" ")
    common_set = list(set(list1) & set(list2))
    for i in list1:
        if i not in common_set and list1.count(i) == 1:
            output.append(i)
    for j in list2:
        if j not in common_set and list2.count(j) == 1:
            output.append(j)
    return output


# s1 = "this apple is sweet"
# s2 = "this apple is sour"
s1 = "apple apple"
s2 = "banana"
print(uncommonFromSentences(s1,s2))
