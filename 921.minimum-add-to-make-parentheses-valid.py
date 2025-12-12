#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        balance = 0
        additions = 0

        for char in s:
            if char == '(':
                balance += 1
            else:  # char == ')'
                if balance > 0:
                    balance -= 1
                else:
                    additions += 1

        return additions + balance
# @lc code=end

