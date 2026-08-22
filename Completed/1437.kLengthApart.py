# 1437. Check If All 1's Are at Least Length K Places Away
# Beats: 23.08%
def kLengthApart(nums, k):
    index = []
    for i in range(len(nums)):
        if nums[i] == 1:
            index.append(i)
        print(index)
        if len(index) > 1:
            print(index[-1], index[-2])
            if index[-1] - index[-2] <= k:
                return False
    return True


nums = [1,0,0,0,1,0,0,1]
k = 2

nums = [1,0,0,1,0,1]
k = 2
print(kLengthApart(nums, k))
