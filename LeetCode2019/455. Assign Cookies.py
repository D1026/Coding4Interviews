"""
发饼干，每个孩子会满足的饼干尺寸 g []
拥有的饼干 s []
输出最多能满足几个孩子，

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

Example 1:
Input: [1,2,3], [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:
Input: [1,2], [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the children,
You need to output 2.
"""


class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        content = 0
        while g and s:
            if s[-1] < g[-1]:
                g.pop()
            else:
                s.pop()
                g.pop()
                content += 1
        return content

