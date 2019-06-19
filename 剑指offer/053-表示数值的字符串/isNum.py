def isInt(s):
    if s[0] in ['+', '-']:
        return isInt(s[1:])
    else:
        for i in s:
            if not i.isdigit():
                return False
        return True


def isNum(s):
    sign = []
    point = []
    hasE = []
    for i in range(len(s)):
        if s[i] in ('+', '-'):
            sign.append(i)
        if s[i] == '.':
            point.append(i)
        if s[i].lower() == 'e':
            hasE.append(i)
    if len(sign) > 2 or len(point) > 1 or len(hasE) > 1:
        return False    # 数量上是否符合，还要检查相对位置上是否符合，+*.*e+*
    if len(sign) == 2:
        if not hasE:
            return False
        elif sign != [0, hasE[0]+1]:
            return False
    if hasE:
        e = hasE[0]
        if point:
            p = point[0]
            if p > e:
                return False
            return (isInt(s[:p]) or not s[:p]) and (isInt(s[p+1:e]) and s[p+1].isdigit()) and isInt(s[e+1:])
        else:
            return isInt(s[:e]) and isInt(s[e+1:])
    else:
        if point:
            p = point[0]
            return isInt(s[:p]) and isInt(s[p+1:]) and s[p+1].isdigit()
        else:
            return isInt(s)

print(isNum('-156.20e+5'))