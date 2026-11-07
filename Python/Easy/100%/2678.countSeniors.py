# 2678. Number of Senior Citizens
# https://leetcode.com/problems/number-of-senior-citizens/description/
# Beats: 100.00%
def countSeniors(self, details: List[str]) -> int:
    count = 0
    for i in details:
        if int(i[11:13]) > 60:
            count += 1
    return count
