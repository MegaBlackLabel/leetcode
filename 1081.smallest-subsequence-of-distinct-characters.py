#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            if char in seen:
                continue
                
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                popped_char = stack.pop()
                seen.remove(popped_char)
                
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)
# @lc code=end

