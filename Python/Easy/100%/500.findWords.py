#500. Keyboard Row
#Beats: 100.00%
def findWords(words):
    output = []
    first = 'qwertyuiop'
    second = "asdfghjkl"
    third = "zxcvbnm"
    for i in range(len(words)):
        print(words[i])
        if words[i][0].casefold() in first:
            check = first
        elif words[i][0].casefold() in second:
            check = second
        else:
            check = third
        for j in range(len(words[i])):
            print(words[i][j], check)
            if words[i][j].casefold() not in check:
                break
        else:
            output.append(words[i])
        print(output)
    return output


# words = ["Hello","Alaska","Dad","Peace"]
words = ["omk"]
print(findWords(words))
