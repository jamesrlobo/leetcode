#2729. Check if The Number is Fascinating
#Beats: 100.00%
def isFascinating(n):
    output = ""
    output += str(n) + str(n*2) +str(n*3)
    fascinating = '123456789'
    for i in output:
        if i not in fascinating or output.count(i) > 1:
            return False
        # if output.count(i) > 1:
        #     return False
    return True


# n = 192
n = 267
print(isFascinating(n))
