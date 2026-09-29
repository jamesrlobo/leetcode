# 2433. Find The Original Array of Prefix Xor
# Beats: 15.36%
def findArray(pref):
    output = [pref[0]]
    # output.append(pref[0])
    for i in range(1, len(pref)):
        output.append(pref[i-1] ^ pref[i])
    return output


pref = [5,2,0,3,1]
# pref = [13]
print(findArray(pref))
x`
