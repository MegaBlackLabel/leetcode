#
# @lc app=leetcode id=3174 lang=python3
#
# [3174] Clear Digits
#

# @lc code=start
class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []
        
        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)
# @lc code=end

