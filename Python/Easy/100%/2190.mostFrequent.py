# 2190. Most Frequent Number Following Key In an Array
# Beats: 100.00%
def mostFrequent(nums, key):
    d = {}
    for i in range(len(nums)-1):
        if nums[i] == key:
            if nums[i+1] not in d:
                d[nums[i+1]] = 1
            else:
                d[nums[i+1]] +=1
    return max(d, key= d.get)


nums = [1,100,200,1,100,1,200,1,200]
key = 1
# nums = [2,2,2,2,3]
# key = 2
print(mostFrequent(nums,key))
