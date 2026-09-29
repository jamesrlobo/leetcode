# 3304. Find the K-th Character in String Game I
# Beats: 29.11%
def kthCharacter(k):
    count = 0
    word = "a"
    while len(word) < k:
        generatedString = ""
        for i in range(len(word)):
            generatedString += (chr(ord(word[i])+1))
        word += generatedString
        count +=1
        print(f"generatedString: {generatedString} | word:{word} | wordlength: {len(word)} | count:{count}")
    return word[k-1]


k = 5
# k = 10
# k = 2
# k = 4 #Expected: c
print(kthCharacter(k))
