#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        opened = []
        pair = [0] * n
        
        for i, char in enumerate(s):
            if char == '(':
                opened.append(i)
            elif char == ')':
                j = opened.pop()
                pair[i] = j
                pair[j] = i
                
        res = []
        curr_index = 0
        direction = 1
        
        while curr_index < n:
            if s[curr_index] in ('(', ')'):
                curr_index = pair[curr_index]
                direction = -direction
            else:
                res.append(s[curr_index])
            
            curr_index += direction
            
        return "".join(res)
# @lc code=end

