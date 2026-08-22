# 2490. Circular Sentence
# Beats: 100.00%
def isCircularSentence(sentence):
    sentence = sentence.split(" ")
    l = len(sentence)
    for i in range(len(sentence)):
        if i+1 < l:
            if sentence[i][-1] != sentence[i+1][0]:
                return False
        else:
            if sentence[i][-1] != sentence[(i+1)%l][0]:
                return False
    return True


# sentence = "leetcode exercises sound delightful"
# sentence = "eetcode"
sentence = "Leetcode is cool"
print(isCircularSentence(sentence))
