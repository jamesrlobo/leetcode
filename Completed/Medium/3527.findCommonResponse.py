# https://leetcode.com/problems/find-the-most-common-response/
# 3527. Find the Most Common Response
# Beats: 83.77%
def findCommonResponse(responses):
    d = {}
    final = []
    for each_item in responses:
        sorted_item = list(set(each_item))
        for item in sorted_item:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1
    maximum = max(d.values())
    for d_item in d:
        if d[d_item] == maximum:
            final.append(d_item)
    return min(final)



responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]
responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]
print(findCommonResponse(responses))


# def findCommonResponse(responses):
#     d = {}
#     new_response = []
#     for i in range(len(responses)):
#         responses[i] = [x for x in set(responses[i])]
#         new_response += responses[i]
#     for k in set(new_response):
#         if new_response.count(k) not in d:
#             d[new_response.count(k)] = [k]
#         else:
#             d[new_response.count(k)] += [k]
#     output = d[max(d)]
#     return min(output)
