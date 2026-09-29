# 434. Number of Segments in a String
# https://leetcode.com/problems/number-of-segments-in-a-string/description/?envType=problem-list-v2&envId=string
# Beats:100.00%
def countSegments(s):
    output = []
    s = s.split(" ")
    print(s)
    for i in s:
        if i != " ":
            output.append(i)
    return len(output)


s = "Hello, my name is John"
# s = ""
# s = "                "
print(countSegments(s))
