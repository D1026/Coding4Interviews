def mul(a):
    if len(a) <= 1:
        return None
    pre = [1]
    for i in range(len(a)-1):
        pre.append(pre[-1]*a[i])
    post = [1]
    for j in range(1, len(a)):
        post.append(post[-1]*a[-j])
    post.reverse()

    print(pre)
    print(post)
    from numpy import array
    return list(array(pre)*array(post))

print(mul([1, 2, 3, 4]))
