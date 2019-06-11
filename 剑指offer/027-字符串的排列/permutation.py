def permutation(s):
    if not s:
        return []
    if len(s) == 1:
        return [s]
    res = []
    for i in range(len(s)):
        # if i+1 == len(s):
        #     subs = permutation(s[:i])
        # else:
        #     subs = permutation(s[:i] + s[i+1:])
        subs = permutation(s[:i] + s[i + 1:])
        for sub in subs:
            res.append(s[i]+sub)

    return res

print(permutation('asd'))