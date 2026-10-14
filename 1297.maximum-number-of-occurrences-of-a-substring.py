#
# @lc app=leetcode id=1297 lang=python3
#
# [1297] Maximum Number of Occurrences of a Substring
#

# @lc code=start
from collections import Counter


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        max_frequency = 0
      
        substring_counter = Counter()
      
        for start_index in range(len(s) - minSize + 1):
            current_substring = s[start_index : start_index + minSize]
          
            unique_chars = set(current_substring)
          
            if len(unique_chars) <= maxLetters:
                substring_counter[current_substring] += 1
                max_frequency = max(max_frequency, substring_counter[current_substring])
      
        return max_frequency
# @lc code=end

