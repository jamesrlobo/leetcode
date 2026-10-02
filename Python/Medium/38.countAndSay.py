# 38. Count and Say
# https://leetcode.com/problems/count-and-say/description/
# Beats: 24.17%
def countAndSay(self, n: int) -> str:
    def helper1(s):
        output = []
        if len(s) == 1:
            output.append([1,1])
        else:
            count = 1
            for i in range(1, len(s)):
                if s[i-1] == s[i]:
                    count += 1
                else:
                    output.append([s[i-1], count])
                    count = 1
            output.append([s[i  ], count])
        return output
    def helper2(output):
        # print(output)
        string = ""
        for j in output:
            string += (str(j[1]) + str(j[0]))
        # print(string)
        return string
    string = "1"
    if n == 1:
        return string
    else:
        for k in range(1, n):
            output = helper1(string)
            string = helper2(output)
    return string
