#2085. Count Common Words With One Occurrence
#Acceptamce: 13.04%
def countWords(words1, words2):
    count = 0
    common_words = set(words1) & set(words2)
    common_words_list = list(common_words)
    print(common_words_list)
    for i in common_words_list:
        if words1.count(i) == words2.count(i) == 1:
            count+=1
    return count


# words1 = ["leetcode","is","amazing","as","is"]
# words2 = ["amazing","leetcode","is"]
# words1 = ["b","bb","bbb"]
# words2 = ["a","aa","aaa"]
# words1 = ["a","ab"]
# words2 = ["a","a","a","ab"]
words1 = ["leetcode","is","leetcode","is","amazing","and","fantastic"]
words2 = ["leetcode","is","leetcode","is","fantastic"]
print(countWords(words1, words2))
