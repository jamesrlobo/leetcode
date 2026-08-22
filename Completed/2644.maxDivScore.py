# 2644. Find the Maximum Divisibility Score
# Beats: 95.86%
def maxDivScore(nums, divisors):
    d = {}
    for i in divisors:
        count = 0
        for j in nums:
            if j%i == 0:
                count += 1
        if count not in d:
            d[count] = [i]
        else:
            d[count] += [i]
    return min(d[max(d)])


nums = [2,9,15,50]
divisors = [5,3,7,2]
print(maxDivScore(nums, divisors))
