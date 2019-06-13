"""
来自编程之美的结论：
第 i 位出现 1 的次数：(0~n-1 编号，即i位权重10^i）
① 第 i 位为 0：由高位决定，高位数 X 10^i
② 第 i 位为1：由高低位同时决定， (高位数 x 10^i) + 低位数+1
③ 第 i 位 > 1: 由高位决定， (高位数+1) x 10^i
"""
def count(x):
    counter = 0
    num = x
    for i in range(len(str(num))):
        digit = num // pow(10, i) % pow(10, i+1)
        high = num//pow(10, i+1)
        low = num % pow(10, i)
        if digit == 0:
            counter += high * pow(10, i)
        if digit == 1:
            counter += high * pow(10, i) + low+1
        if digit > 1:
            counter += (high+1) * pow(10, i)
    return counter

print(count(12))
print(count(123))