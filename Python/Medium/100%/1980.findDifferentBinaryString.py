# 1980. Find Unique Binary String
# Beats: 100.00%
def findDifferentBinaryString(nums):
    n = len(nums[0])
    minimum = (int(("0"*n), 2))
    maximum = (int(("1"*n), 2))
    for i in range(minimum, maximum+1):
        if (bin(i)[2:].zfill(n)) not in nums:
            return bin(i)[2:].zfill(n)


nums = ["01","10"]
nums = ["0"]
print(findDifferentBinaryString(nums))
