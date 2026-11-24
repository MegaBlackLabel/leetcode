#
# @lc app=leetcode id=1347 lang=python3
#
# [1347] Minimum Number of Steps to Make Two Strings Anagram
#

# @lc code=start
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        char_count = Counter(s)
      
        steps_needed = 0
      
        for char in t:
            char_count[char] -= 1
          
            if char_count[char] < 0:
                steps_needed += 1
      
        return steps_needed
# @lc code=end

