# 468. Validate IP Address
# https://leetcode.com/problems/validate-ip-address/description/
# Beats: 100.00%
def validIPAddress(self, queryIP: str) -> str:
    if "." in queryIP and ":" in queryIP:
        return "Neither"
    elif "." in queryIP:
        queries = queryIP.split(".")
        # print(queries)
        if len(queries) != 4:
            return "Neither"
        for i in queries:
            if i == "":
                return "Neither"
            for j in i:
                if j not in "0123456789":
                    return "Neither"
            if int(i) < 0 or int(i) > 255:
                return "Neither"
            if len(i) != len(str(int(i))):
                return "Neither"
        return "IPv4"
    elif ":" in queryIP:
        queries = queryIP.split(":")
        # print(queries)
        if len(queries) != 8:
            return "Neither"
        for i in queries:
            if len(i) < 1 or len(i) > 4:
                return "Neither"
            if i == "":
                return "Neither"
            for j in i:
                if j not in "0123456789ABCDEFabcdef":
                    return "Neither"
        return "IPv6"
    else:
        return "Neither"
