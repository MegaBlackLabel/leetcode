#
# @lc app=leetcode id=1003 lang=python3
#
# [1003] Check If Word Is Valid After Substitutions
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) >= 3 and ''.join(stack[-3:]) == 'abc':
                stack.pop()
                stack.pop()
                stack.pop()
        return len(stack) == 0
# @lc code=end

