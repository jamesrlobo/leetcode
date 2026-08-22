# 2094. Finding 3-Digit Even Numbers
#Beats: 58.76%
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        output, possible = [], []
        for x in range(100, 999):
            if x%2 == 0:
                possible.append(x)
        for i in possible:
            for j in str(i):
                if str(i).count(j) > digits.count(int(j)):
                    break
            else:
                output.append(i)
        return output
