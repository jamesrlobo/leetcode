# 748. Shortest Completing Word
# Beats: 73.15%
def shortestCompletingWord(licensePlate, words):
    newLicensePlate = ""
    for ch in licensePlate:
        if ch.isalpha():
            newLicensePlate += ch.casefold()
    print("newLicensePlate:", newLicensePlate)
    output = []
    for word in words:
        for i in set(newLicensePlate):
            if i not in word or newLicensePlate.count(i) > word.count(i):
                break
        else:
            output.append(word)
    print("output:", output)
    if len(output) > 1:
        finalOutput = output[0]
        for item in range(1, len(output)):
            if len(finalOutput) > len(output[item]):
                finalOutput = output[item]
    else:
        finalOutput = output[0]
    return finalOutput


licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]

licensePlate = "1s3 456"
words = ["looks","pest","stew","show"]

licensePlate = "TE73696"
words = ["ten","two","better","talk","suddenly","stand","protect","collection","about","southern"]

licensePlate = "GrC8950"
words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]
print(shortestCompletingWord(licensePlate, words))
