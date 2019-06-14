def firstSingle(s):
    from collections import OrderedDict
    dic = OrderedDict()
    # dic = dict()  # --- python 3.7 以后，内置类型 dict() 也可以记住 keys 添加顺序
    for i in s:
        dic[i] = dic.get(i, 0) + 1
    print(dic)
    while True:
        k, v = dic.popitem(last=False)
        if v == 1:
            return k




print(firstSingle('asdfgnaggdnjs'))