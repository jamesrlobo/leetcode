# 1807. Evaluate the Bracket Pairs of a String
# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
# Beats: 5.00%
def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
    d = {}
    for x in knowledge:
        d[x[0]] = x[1]
    start, end = -1, -1
    words, indices = [], []
    for i in range(len(s)):
        if s[i] == "(":
            start = i+1
        elif s[i] == ")":
            end = i
        if end > 0:
            words.append(s[start:end])
            indices.append([start-1, end+1])
            start = -1
            end = -1
    words = words[::-1]
    indices = indices[::-1]
    for m in range(len(words)):
        if words[m] in d:
            s = (s[:indices[m][0]] + d[words[m]] + s[indices[m][1]:])
        else:
            s = (s[:indices[m][0]] + '?' + s[indices[m][1]:])
    return s
