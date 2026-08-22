# 3895. Count Digit Appearances
# https://leetcode.com/problems/count-digit-appearances/description/
# Beats: 82.81%
def countDigitOccurrences(nums, digit):
    output = 0
    digit = str(digit)
    for i in nums:
        i = str(i)
        if i.count(digit):
            output += (str(i).count(digit))
    return output


nums = [12,54,32,22]
digit = 2
print(countDigitOccurrences(nums, digit))
