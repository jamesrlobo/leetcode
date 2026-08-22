# https://leetcode.com/problems/simplified-fractions/description/?envType=problem-list-v2&envId=math
# 1447. Simplified Fractions
# Beats: 86.17%
import math
def simplifiedFractions(n):
    output = []
    numerator = [x for x in range(1, n+1)]
    denominator = [x for x in range(2, n+1)]
    for i in numerator:
        for j in denominator:
            if i < j and math.gcd(i,j) == 1:
                output.append(str(i)+"/"+str(j))
    return output


n = 4
print(simplifiedFractions(n))
