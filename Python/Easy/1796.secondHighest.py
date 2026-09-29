# 1796. Second Largest Digit in a String
def secondHighest(s):
    output = []
    for i in s:
        if i.isdigit():
            output.append(i)
    output = (set(output))
    if len(output) == 0:
        return -1
    elif len(output) == 1:
        return -1
    else:
        output = sorted(output)
        output.pop()
    return output.pop()



# s = "dfa12321afd"
# s = "abc1111"
# s = "xyz"
# s = "sjhtz8344"
# s = "vwkxfq9791769"
print(secondHighest(s))
