class Solution:
    def primes(self, n: int):
        res = []
        if n <= 1:
            return res
        nums = [None] * (n+1)
        nums[0] = False
        nums[1] = False

        for i in range(n+1):
            if nums[i] is None:
                nums[i] = True

                for j in range(2*i, n+1, i):
                    nums[j] = False
        print(nums)
        return [i for i in range(n+1) if nums[i] is True]

print(Solution().primes(11))


# def getNprimes(self, n: int):
#     flags = {0: False, 1: False}
#     res = []
#
#     i = 0
#     while len(res) < n:
#         i += 1
#         if i not in flags.keys():
#             flags[i] = True
#             res.append(i)
#
# 如果求前 N 个质数，很难办，因为无法去定 标记 质数 的 m 倍，这个 m 标记到什么范围为止；因此还是以某种策略 调用 上面这个函数获得。