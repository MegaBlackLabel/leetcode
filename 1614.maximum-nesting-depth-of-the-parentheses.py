#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        opened = 0

        for c in s:
            if c == '(':
                opened += 1
                ans = max(ans, opened)
            elif c == ')':
                opened -= 1

        return ans
# @lc code=end

