# 3024. Type of Triangle
# Beats: 100.00%
def triangleType(nums):
    #check if its valid
    nums = sorted(nums)
    if nums[2] < nums[0] + nums[1]:
        #check type of triangle
        if len(set(nums)) == 1:
            return "equilateral"
        elif len(set(nums)) == 2:
            return "isosceles"
        else:
            return "scalene"
    else:
        return "none"


nums = [3,3,3]
nums = [3,4,5]
print(triangleType(nums))
