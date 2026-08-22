# 2299. Strong Password Checker II
# Beats: 100.00%
def strongPasswordCheckerII(password):
    lower = "'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'"
    upper = "'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'"
    special_chars = "!@#$%^&*()-+"
    numbers = "'0','1','2','3','4','5','6','7','8','9'"
    if len(password) < 8:
        return False
    lower_check, upper_check, ch_check, num_check = 0, 0, 0, 0
    for i in range(len(password)):
        if password[i] in lower:
            lower_check = 1
        if password[i] in upper:
            upper_check = 1
        if password[i] in special_chars:
            ch_check = 1
        if password[i] in numbers:
            num_check = 1
        if i != len(password)-1:
            if password[i] == password[i+1]:
                return False
    if lower_check == upper_check == ch_check == num_check == 1:
        return True
    return False


password = "IloveLe3tcode!"
password = "Me+You--IsMyDream"
password = "1aB!"
print(strongPasswordCheckerII(password))
