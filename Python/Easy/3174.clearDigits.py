# 3174. Clear Digits
def clearDigits(s):
    characters = list(s)
    output = [characters[0]]
    for i in range(1, len(characters)):
        if characters[i].isdigit():
            output.pop()
        else:
            output.append(characters[i])
    return "".join(output)


s = "cb34"
# s = "abc"
print(clearDigits(s))
