# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/
# Beats: 83.13%
def groupAnagrams(strs):
    output = {}
    for i in strs:
        temp = "".join(sorted(list(i)))
        if temp not in output:
            output[temp] = [i]
        else:
            output[temp] += [i]
    final = list(output.values())
    return final


strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]
print(groupAnagrams(strs))

# def groupAnagrams(strs):
#     output = []
#     i = 0
#     while i < (len(strs)):
#         # print(strs[i])
#         temp = [strs[i]]
#         # print("--")
#         j = i+1
#         while j < len(strs):
#             # print(strs[i], strs[j], j)
#             if sorted(list(strs[i])) == sorted(list(strs[j])):
#                 temp.append(strs[j])
#                 strs.pop(j)
#                 # print(strs[j], j, temp)
#             else:
#                 j +=1
#         output.append(temp)
#         temp = []
#         i+=1
#     return output
