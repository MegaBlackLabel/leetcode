#
# @lc app=leetcode id=1318 lang=python3
#
# [1318] Minimum Flips to Make a OR b Equal to c
#

# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flip_count = 0
      
        for bit_position in range(32):
            bit_a = (a >> bit_position) & 1
            bit_b = (b >> bit_position) & 1
            bit_c = (c >> bit_position) & 1
            if bit_c == 0:
                flip_count += bit_a + bit_b
            else:
                flip_count += int(bit_a == 0 and bit_b == 0)
      
        return flip_count
# @lc code=end

