# 2451. Odd String Difference
# Beats: 100.00%
def oddString(words):
    difference = []
    for word in words:
        print(word)
        temp = [0]* (len(word)-1)
        for ch in range(len(word)-1):
            temp[ch] = (ord(word[ch+1])-97) - (ord(word[ch])-97)
        print(temp)
        difference.append(temp)
    print(difference)
    for i in difference:
        if difference.count(i) == 1:
            return words[difference.index(i)]


words = ["adc","wzy","abc"]
words = ["aaa","bob","ccc","ddd"]
words = ["jijij","yxyxy","edede","edede","bbaaa","kjkjk"]
print(oddString(words))
