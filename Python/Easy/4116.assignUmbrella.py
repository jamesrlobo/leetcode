# 4116. Assign Umbrella on Rainy Days
# https://leetcode.com/problems/assign-umbrella-on-rainy-days/description/
# Beats: 62.07%
def assignUmbrella(self, rain: list[int]) -> list[str]:
    output = []
    aliceCount, bobCount = 0, 0
    n = len(rain)
    for i in range(n-1):
        if rain[i] == 1 and rain[i+1] == 1:
            if aliceCount > bobCount:
                output.append("Bob")
                bobCount += 1
            else:
                output.append("Alice")
                aliceCount += 1
        elif rain[i] == 1 and rain[i+1] == 0:
            output.append("Bob")
            bobCount += 1
        else:
            output.append("None")
    if rain[-1] == 1:
        output.append("Bob")
    else:
        output.append("None")
    return output
