def match(s1, s2):
    # s1 - 表达式，s2 - str
    if not s1 and not s2:
        return True
    if not s1 and s2:
        return False
    if len(s1) == 1:
        return len(s2) == 1 and (s1 == s2 or s1 == '.')
    if len(s1) == 2 and s1[1] == '*' and not s2:
        return True

    # len(s1)>=2,s2 不为空的情况
    i, j = 0, 0
    if s1[i+1] == '*':
        if s1[i] == s2[j] or s1[i] == '.':
            return match(s1[2:], s2[1:]) or match(s1, s2[1:]) or match(s1[2:], s2)
        else:
            return match(s1[2:], s2)
    elif s1[i] == s2[j] or s1[i] == '.':
        return match(s1[1:], s2[1:])

print(match('ab*', 'abbb'))
print(match('a.*c', 'azzzzc'))