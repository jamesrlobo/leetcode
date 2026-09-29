# 844. Backspace String Compare
def backspaceCompare(s,t):
    s = list(s)
    t = list(t)
    i = 0
    while i < len(s):
        if s[i] == "#":
            s.pop(i)
            if i-1 >= 0:
                s.pop(i-1)
            i = 0
        else:
            i+=1
        print(s)
    j = 0
    while j < len(t):
        if t[j] == "#":
            t.pop(j)
            if j-1 >= 0:
                t.pop(j-1)
            j = 0
        else:
            j+=1
        print(t)
    print("".join(s), "".join(t))
    return "".join(s) == "".join(t)


# s = "y#fo##f"
# t = "y#f#o##f"
# s = "ab#c"
# t = "ad#c"
# s = "ab##"
# t = "c#d#"
# s = "a#c"
# t = "b"
print(backspaceCompare(s,t))
