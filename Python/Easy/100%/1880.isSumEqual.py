# 1880. Check if Word Equals Summation of Two Words
def isSumEqual(firstWord, secondWord, targetWord):
    first = [int(ord(x)-97) for x in firstWord]
    # first_num = int(''.join(map(str, first)))
    second = [int(ord(x)-97) for x in secondWord]
    # second_num = int(''.join(map(str, second)))
    target = [int(ord(x)-97) for x in targetWord]
    # target_num = int(''.join(map(str, target)))
    return int(''.join(map(str, first))) + int(''.join(map(str, second))) == int(''.join(map(str, target)))


# firstWord = "acb"
# secondWord = "cba"
# targetWord = "cdb"
# firstWord = "aaa"
# secondWord = "a"
# targetWord = "aab"
firstWord = "aaa"
secondWord = "a"
targetWord = "aaaa"
print(isSumEqual(firstWord, secondWord, targetWord))
