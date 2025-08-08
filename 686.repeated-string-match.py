#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#

# @lc code=start
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        
        min_repeats = (len(b) + len(a) - 1) // len(a)
        
        if b in a * min_repeats:
            return min_repeats
        
        if b in a * (min_repeats + 1):
            return min_repeats + 1
        
        return -1
# @lc code=end

