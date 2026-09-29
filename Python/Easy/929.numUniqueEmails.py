929. Unique Email Addresses
Beats: 45.89%
def numUniqueEmails(emails):
    output = []
    for i in emails:
        localName = i.split('@')
        newLocalName = ""
        for ch in localName[0]:
            if ch != "." and ch != "+":
                newLocalName += ch
            elif ch == "+":
                break
        test = newLocalName+"@"+localName[1]
        if test not in output:
            output.append(test)
    return len(output)


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
print(numUniqueEmails(emails))
