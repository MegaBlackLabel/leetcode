#
# @lc app=leetcode id=3120 lang=python3
#
# [3120] Count the Number of Special Characters I
#

# @lc code=start
from string import ascii_lowercase, ascii_uppercase


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        char_set = set(word)
      
        special_count = sum(
            lower_char in char_set and upper_char in char_set 
            for lower_char, upper_char in zip(ascii_lowercase, ascii_uppercase)
        )
      
        return special_count

# @lc code=end

