#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#

# @lc code=start
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        def is_valid_first_byte(byte: int) -> int:
            if byte & 0b10000000 == 0:
                return 1
            elif byte & 0b11100000 == 0b11000000:
                return 2
            elif byte & 0b11110000 == 0b11100000:
                return 3
            elif byte & 0b11111000 == 0b11110000:
                return 4
            else:
                return -1

        i = 0
        while i < len(data):
            first_byte = data[i]
            num_bytes = is_valid_first_byte(first_byte)
            if num_bytes == -1 or i + num_bytes > len(data):
                return False

            for j in range(1, num_bytes):
                if data[i + j] & 0b11000000 != 0b10000000:
                    return False

            i += num_bytes

        return True
# @lc code=end

