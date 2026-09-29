# 3591. Check if Any Element Has Prime Frequency
# Beats: 17.65%
def checkPrimeFrequency(nums):
    freq = []
    for i in set(nums):
        freq.append(nums.count(i))
    print(set(freq))
    if set(freq) == {1}:
        return False
    for j in set(freq):
        if j == 2:
            return True
        elif j > 2:
            for k in range(2, j):
                print(j, k)
                if j%k == 0:
                    return False
    return True


# nums = [1,2,3,4,5,4]
# nums = [1,2,3,4,5]
# nums = [2,2,2,4,4]
nums = [3,0,3,6,3,3]
print(checkPrimeFrequency(nums))
# n = 8
#
# for i in range(2, n):
#     if n%i == 0:
#         print(i)
