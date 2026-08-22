# 2748. Number of Beautiful Pairs
# Beats: 10.15%
def countBeautifulPairs(nums):
    output = 0
    def gcd(x, y):
        result = min(x, y)
        while result > 0:
            if x % result == 0 and y % result == 0:
                break
            result -= 1
        return result
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                if gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])) ==  1:
                    output += 1
    return output


nums = [2,5,1,4]
nums = [11,21,12]
nums = [31,25,72,79,74]
print(countBeautifulPairs(nums))
