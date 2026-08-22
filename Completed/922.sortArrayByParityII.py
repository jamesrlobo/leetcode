# 922. Sort Array By Parity II
# Beats : 31.85%
def sortArrayByParityII(nums):
    output = []
    odd = [x for x in nums if x%2 !=0]
    even = [x for x in nums if x%2 ==0]
    for i in range(len(nums)):
        if i%2 == 0:
            output.append(even.pop())
        else:
            output.append(odd.pop())
    return output


nums = [4,2,5,7]
print(sortArrayByParityII(nums))
