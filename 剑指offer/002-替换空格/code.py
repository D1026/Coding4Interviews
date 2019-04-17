

def replaceSpace(s):
    sl = []
    for i in s:
        sl.append(i)
    for index in range(len(sl)):
        if sl[index] == ' ':
            sl[index] = '%20'
    return ''.join(sl)
print(replaceSpace('We Are Happy'))

# python built in type 'str'
s = 'SKT T1 have won the World Championship three times'
ss = s.replace(' ', '%20')
print(ss)
