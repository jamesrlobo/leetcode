# 2164. Sort Even and Odd Indices Independently
# Beats: 100%
def sortEvenOdd(nums):
    output, even, odd = [], [], []
    for i in range(len(nums)):
        if i%2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    even.sort()
    odd.sort(reverse=True)
    l = min(len(even), len(odd))
    for i in range(l):
        output.append(even[i])
        output.append(odd[i])
    if len(even) > len(odd):
        output += (even[l:])
    else:
        odd += (odd[l:])
    return output

# nums = [4,1,2,3]
# nums = [2,1]
nums = [5,39,33,5,12,27,20,45,14,25,32,33,30,30,9,14,44,15,21]
print(sortEvenOdd(nums))
