"""
Given an array of numbers nums, in which exactly two elements appear only once
and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
#   这种方法太魔性了，对二进制运算性质要求太高
class Solution(object):
    def singleNumber(self, nums):
        from functools import reduce
        r = reduce(lambda a,b:a^b, nums)
        ii = r ^ r & (r-1)  # last set bit, 把 a^b 除了最后一个 1，其它位全部制0
        a = 0
        b = 0
        for num in nums:
            if num & ii:
                a ^= num
            else:
                b ^= num
        return [a^r, b^r]


#   Time Complexity O(n) Space-complex O(n-2),实际上空间复杂度应该平均在常数
class Solution(object):
    def singleNumber(self, nums):
        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)

        return list(s)
