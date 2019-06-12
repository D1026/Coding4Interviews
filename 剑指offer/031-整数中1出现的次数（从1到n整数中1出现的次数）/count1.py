def count(x):
    n = len(str(x))
    high = x % pow(10, n-1)
    cot = 0
    for i in range(n-1):
        post = x % pow(10, n-1) + 1
        pre = x // pow(10, n-i-1) + 1
        cot += pre * post
    cot += x % pow(10, n-1) + 1

    return cot

print(count(12))
print(count(10))