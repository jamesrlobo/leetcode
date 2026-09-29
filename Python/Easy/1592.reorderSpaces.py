# 1592. Rearrange Spaces Between Words
#Beats: 5.13%
def reorderSpaces(text):
    output = ""
    spaces = text.count(" ")
    word = text.split(" ")
    i = 0
    while i < len(word):
        if word[i] == "":
            word.pop(i)
        else:
            i += 1
    print("No. of spaces:", spaces)
    print("No. of words:", len(word))
    if len(word) == 1:
        return (word[0] + (("_")*spaces))
    spaces_to_add = int(spaces/(len(word)-1))
    extra_Spaces = int(spaces%(len(word)-1))
    print("Spaces to add:", spaces_to_add)
    print("Extra spaces:", extra_Spaces)
    for j in range(len(word)-1):
        output += word[j] + (("_")*spaces_to_add)
    output += word[-1] + (("_")*extra_Spaces)
    return output




# text = "  this   is  a sentence "
# text = " practice   makes   perfect"
# text = "a"
text = "  hello"
print(reorderSpaces(text))
