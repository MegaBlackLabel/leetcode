#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        opened = 0

        for c in s:
            if c == '(':
                opened += 1
                if opened > 1:
                    ans.append(c)
            else:  # c == ')'
                opened -= 1
                if opened > 0:
                    ans.append(c)

        return ''.join(ans)
# @lc code=end

