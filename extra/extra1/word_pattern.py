def findPattern(p, s):
    s = s.split(" ")
    if len(p) != len(s):
        return False
    pattern = {}
    for i in range(len(p)):
        if p[i] not in pattern:
            pattern[p[i]] = s[i]
        elif pattern[p[i]] != s[i]:
            return False
    return True