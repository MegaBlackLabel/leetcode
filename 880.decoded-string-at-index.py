#
# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#

# @lc code=start
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        
        size = 0

        # Find size = length of decoded string
        for char in s:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1

        for i in range(len(s) - 1, -1, -1):
            k %= size
            char = s[i]

            if k == 0 and char.isalpha():
                return char

            if char.isdigit():
                size //= int(char)
            else:
                size -= 1
# @lc code=end

