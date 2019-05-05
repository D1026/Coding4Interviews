def skipSteps(n):
    f1 = 1
    f2 = 2
    if n == 1:
        return f1
    if n == 2:
        return f2
    for i in range(n-2):
        f2, f1 = f2 + f1, f2
    return f2

print(skipSteps(7))