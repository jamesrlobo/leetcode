# 1018. Binary Prefix Divisible By 5
#Beats: 13.52%
def prefixesDivBy5(nums):
    s = ""
    output = []
    for i in range(len(nums)):
        s += str(nums[i])
        if (int(s,2)%5) == 0:
            output.append(True)
        else:
            output.append(False)
    return output


# nums = [0,1,1]
# nums = [1,1,1]
# nums = [0,1,1,1,1,1]
nums = [1,1,1,0,1]
print(prefixesDivBy5(nums))
