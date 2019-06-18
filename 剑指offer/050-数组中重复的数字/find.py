"""
思路1：O(n),O(n),扫描检查加入hashTable
思路2：O(n),O(1),0-n-1，无重复则排序后有 i = a[i], if a[i] = m ,swap(a[i], a[m])

"""
def find(a):
    i = 0
    while True:
        if i == a[i]:
            i += 1
        elif a[a[i]] == a[i]:
            return a[i]
        else:
            m = a[i]
            a[i], a[m] = a[m], a[i]

print(find([2, 3, 1, 0, 2, 5, 3]))
