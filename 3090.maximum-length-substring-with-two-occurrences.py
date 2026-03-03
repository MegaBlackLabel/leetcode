#
# @lc app=leetcode id=3090 lang=python3
#
# [3090] Maximum Length Substring With Two Occurrences
#

# @lc code=start
import collections


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        count = collections.Counter()
        left_ptr = 0
        max_length = 0

        for right_ptr, char in enumerate(s):
            count[char] += 1

            while count[char] > 2:
                left_char = s[left_ptr]
                count[left_char] -= 1
                left_ptr += 1

            max_length = max(max_length, right_ptr - left_ptr + 1)

        return max_length
# @lc code=end

