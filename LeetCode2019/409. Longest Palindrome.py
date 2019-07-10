""""
Easy

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"
Output:
7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7."""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        odd = False
        res = 0
        from collections import Counter
        count = Counter(s)
        for k, v in count.items():
            if v%2 == 0:
                res += v
            else:
                res += v-1
                odd = True
        if odd:
            res += 1
        return res
    
"""
Runtime: 40 ms, faster than 55.83% of Python3 online submissions for Longest Palindrome.
Memory Usage: 13.2 MB, less than 32.80% of Python3 online submissions for Longest Palindrome.
"""

print(Solution().longestPalindrome('aabc'))