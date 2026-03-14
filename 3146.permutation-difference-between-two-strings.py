#
# @lc app=leetcode id=3146 lang=python3
#
# [3146] Permutation Difference between Two Strings
#

# @lc code=start
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
        s_indices = {char: i for i, char in enumerate(s)}   
 
        difference_sum = 0
        for i, char in enumerate(t):
            s_index = s_indices[char]
            difference_sum += abs(s_index - i)
            
        return difference_sum
# @lc code=end

