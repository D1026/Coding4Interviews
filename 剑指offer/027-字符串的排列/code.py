
def helper(s):
    if len(s) == 1:
        print(type(s[0]))
        return s[0]    # 单个字符也是字符串对象，可迭代
    res = []
    for i in range(len(s)):
        l = helper(s[:i] + s[i+1:])   # 字符串，不会越界 s[9999:] = s[max_index:]
        for j in l:
            res.append(s[i] + j)

    return res

def Permutation(ss):
    # write code here
    if not ss: return []
    words = list(ss)
    return list(sorted(set(helper(words))))

print(Permutation('ab'))
