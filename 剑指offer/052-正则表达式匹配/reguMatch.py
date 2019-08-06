def match(s1, s2):
    # s1 - 表达式，s2 - str
    if not s1 and not s2:
        return True
    if not s1 and s2:
        return False
    if len(s1) == 1:
        return len(s2) == 1 and (s1 == s2 or s1 == '.')
    if not s2:
        if len(s1) % 2 != 0:
            return False
        else:
            for i in range(len(s1)//2):
                if s1[2*i+1] != '*':
                    return False
            return True

    # len(s1)>=2,s2 不为空的情况
    if s1[1] == '*':
        if s1[0] == s2[0] or s1[0] == '.':
            return match(s1[2:], s2[1:]) or match(s1, s2[1:]) or match(s1[2:], s2)
        else:
            return match(s1[2:], s2)
    elif s1[0] == s2[0] or s1[0] == '.':
        return match(s1[1:], s2[1:])
    else:
        return False

print(match('ab*', 'abbb'))
print(match('a.*c', 'azzzzc'))
print(match('a*a*', ''))
print(match('abcd', 'qbcd'))