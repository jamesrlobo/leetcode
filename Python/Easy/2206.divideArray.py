# 2206. Divide Array Into Equal Pairs
def divideArray(nums):
    count = []
    for i in set(nums):
        count.append(nums.count(i))
    for j in count:
        if j%2 != 0:
            return False
    return True


nums = [3,2,3,2,2,2]
# nums = [1,2,3,4]
# nums = [18,19,5,5,18,19,5,6,12,19,13,4,16,11,4,16,10,8,12,8,2,1,8,17,4,18,3,5,16,2,16,12,17,16,7,16,2,17,19,9,1,20,17,17,4,6]
print(divideArray(nums))
