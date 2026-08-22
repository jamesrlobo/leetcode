
def getSneakyNumbers(nums):
    output = []
    for i in set(nums):
        if nums.count(i) > 1:
            output.append(i)
    return output


# nums = [0,1,1,0]
nums = [0,3,2,1,3,2]
print(getSneakyNumbers(nums))
