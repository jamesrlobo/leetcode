# 2455. Average Value of Even Numbers That Are Divisible by Three
# Beats: 100.00%
def averageValue(nums):
    output = []
    for i in nums:
        if i%6 == 0:
            output.append(i)
    print(output)
    if len(output) == 0:
        return 0
    return int(sum(output)/len(output))


nums = [1,3,6,10,12,15]
nums = [1,2,4,7,10]
nums = [43,9,75,76,25,96,46,85,19,29,88,2,5,24,60,26,76,24,96,82,97,97,72,35,21,77,82,30,94,55,76,94,51]
print(averageValue(nums))
