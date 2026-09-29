# 1233. Remove Sub-Folders from the Filesystem
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/
# Beats: 5.25%
def removeSubfolders(folder):
    # Sort the folders lexicographically.
    folder = sorted(folder)
    # print(folder)
    # Insert the current element in an array and then loop until we get rid of all of their subfolders, repeat this until no element is left.
    i = 0
    while i < len(folder):
        print("Curr:", folder[i])
        curr = folder[i]
        j = i+1
        while j < len(folder):
            comp = folder[j]
            print(curr, comp)
            if curr+"/" == comp[:len(curr)+1]:
                folder.pop(j)
            else:
                j += 1
        i+=1
    return folder


folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# folder = ["/a","/a/b/c","/a/b/d"]
# folder = ["/a/b/c","/a/b/ca","/a/b/d"]
# folder = ["/c","/d/c/e"] #Expected: ["/c","/d/c/e"]
# folder = ["/a", "/ab/a"] #["/a","/ab/a"]
print(removeSubfolders(folder))
