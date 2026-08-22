# 1720. Decode XORed Array
# Beats: 81.91%
def decode(encoded, first):
    output = []
    output.append(first)
    for i in range(len(encoded)):
        output.append(encoded[i] ^ output[i] )
    return output


encoded = [1,2,3]
first = 1

encoded = [6,2,7,3]
first = 4
print(decode(encoded, first))
