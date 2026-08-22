def canBeTypedWords(text, brokenLetters):
    text = text.split()
    output = len(text)
    for i in text:
        print("i:", i)
        for j in i:
            print("j:", j)
            if j in brokenLetters:
                output -=1
                break
    return output


# text = "hallo world"
# brokenLetters = "ad"
text = "leet code"
brokenLetters = "e"
print(canBeTypedWords(text, brokenLetters))
