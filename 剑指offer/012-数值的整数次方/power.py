a = 10  # 1010
print(bin(a))
print(bin(a >> 1))
print(bin(a >> 2))
# --- output ---
# 0b1010
# 0b101
# 0b10
def power(base, exp):
    if exp == 0:
        return 1
    flag = 0
    if exp < 0:
        flag = 1
        exp = -exp
    pow = 1
    while exp:
        if exp & 1:
           pow *= base
        exp = exp >> 1
        base *= base

    return pow if not flag else 1/pow

print(power(2, -3))