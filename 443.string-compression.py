#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        
        n = len(chars)
        if n == 1:
            return 1

        write = 0
        read = 0

        while read < n:
            chars[write] = chars[read]
            write += 1
            count = 1

            while read + 1 < n and chars[read] == chars[read + 1]:
                read += 1
                count += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            read += 1

        return write

# @lc code=end

