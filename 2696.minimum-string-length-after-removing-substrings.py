#
# @lc app=leetcode id=2696 lang=python3
#
# [2696] Minimum String Length After Removing Substrings
#

# @lc code=start
class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        def match(c: str) -> bool:
            return stack and stack[-1] == c

        for c in s:
            if c == 'B' and match('A'):
                stack.pop()
            elif c == 'D' and match('C'):
                stack.pop()
            else:
                stack.append(c)

        return len(stack)
# @lc code=end

