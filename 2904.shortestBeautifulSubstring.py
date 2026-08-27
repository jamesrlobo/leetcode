# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/
def shortestBeautifulSubstring(s, k):
    if k == 1 and s.count("1") > 0:
        return "1"
    n = len(s)
    output = ""
    position = []
    for i in range(n):
        if s[i] == "1":
            position.append(i)
    if len(position) == 0:
        return ""
    for x in position:
        for y in position:
            if x < y:
                temp = (s[x:y+1])
                if temp.count("1") == k:
                    # print(temp, temp.count("1"))
                    if output == "":
                        output = temp
                    else:
                        if len(temp) < len(output):
                            output = temp
    return output


s = "100011001"
k = 3
# s = "1011"
# k = 2
# s = "000"
# k = 1
# s = "11000111"
# k = 1
print(shortestBeautifulSubstring(s, k))
