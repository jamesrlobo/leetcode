# 811. Subdomain Visit Count
# https://leetcode.com/problems/subdomain-visit-count/description/
# Beats: 100.00%
def subdomainVisits(cpdomains):
    final = []
    d = {}
    for domain in cpdomains:
        domain = domain.split(" ")
        # print(domain)
        text1 = int(domain[0])
        text2 = domain[1]
        text2 = text2.split(".")
        # print(text1)
        # print(text2)
        text2 = text2[::-1]
        output = ""
        for i in range(len(text2)):
            if i == 0:
                output = text2[i]
            else:
                output = text2[i] + "." + output
            if output not in d:
                d[output] = text1
            else:
                d[output] += text1
    for item in d:
        final.append(str(d[item]) +" "+ str(item))
    return final


cpdomains = ["9001 discuss.leetcode.com"]
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# cpdomains = ["900 google.mail.com"]
print(subdomainVisits(cpdomains))

# def subdomainVisits(cpdomains):
#     final = []
#     for i in cpdomains:
#         temp = i.split(" ")
#         # print(temp)
#         word1 = temp[0]
#         word2 = temp[1]
#         temp1 = word2.split(".")
#         # print(temp1)
#         x = 0
#         temp1 = temp1[::-1]
#         output = ""
#         while x < len(temp1):
#             if len(output) > 0:
#                 output = (temp1[x]) + "."+ output
#             else:
#                 output = (temp1[x])
#             final.append(word1+" "+output)
#             x += 1
#     return final
