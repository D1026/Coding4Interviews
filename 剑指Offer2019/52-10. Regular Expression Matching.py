"""
Hard
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p and not s:
            return True
        if not p and s:
            return False
        if len(p) == 1:
            return len(s) == 1 and (s == p or p == '.')
        if not s:
            if len(p)%2 != 0:
                return False
            else:
                for i in range(len(p)//2):
                    if p[2*i+1] != '*':
                        return False
                return True
        # len(p) >= 2, len(s) >=1
        if p[1] == '*':
            if p[0] == s[0] or p[0] == '.':
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s, p[2:])
        elif p[0] == s[0] or p[0] == '.':
            return self.isMatch(s[1:], p[1:])
        else:
            return False

print(Solution().isMatch('aa', 'a*'))
print(Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))

