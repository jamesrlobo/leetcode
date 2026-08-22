# 1078. Occurrences After Bigram
# Beats: 100.00%
def findOcurrences(text, first, second):
    output = []
    words = text.split()
    for i in range(len(words)-2):
        if words[i] == first and words[i+1] == second:
            output.append(words[i+2])
    return output


text = "alice is a good girl she is a good student"
first = "a"
second = "good"

text = "we will we will rock you"
first = "we"
second = "will"
print(findOcurrences(text, first, second))
