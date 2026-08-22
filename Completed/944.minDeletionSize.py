# 944. Delete Columns to Make Sorted
# Beats: 46.74%
def minDeletionSize(strs):
    output = 0
    for i in range(len(strs[0])):
        temp = []
        for j in range(len(strs)):
            temp.append(ord(strs[j][i]))
        if temp != sorted(temp):
            output +=1
    return output


strs = ["cba","daf","ghi"]
strs = ["a","b"]
strs = ["zyx","wvu","tsr"]
strs = ["rrjk","furt","guzm"]
print(minDeletionSize(strs))
