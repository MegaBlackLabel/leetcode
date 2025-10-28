#
# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#

# @lc code=start
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        total_shift = 0
        s_list = list(s)

        for i in range(len(shifts) - 1, -1, -1):
            total_shift = (total_shift + shifts[i]) % 26
            original_char = s_list[i]
            shifted_char = chr(
                (ord(original_char) - ord('a') + total_shift) % 26 + ord('a')
            )
            s_list[i] = shifted_char

        return ''.join(s_list)
# @lc code=end

