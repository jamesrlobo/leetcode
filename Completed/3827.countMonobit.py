# 3827. Count Monobit Integers
# Beats: 13.66%
def countMonobit(n):
    output = 0
    for i in range(n+1):
        if len(set(bin(i)[2:])) == 1:
            output += 1
    return output


n = 4
print(countMonobit(n))
