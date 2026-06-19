#
# @lc app=leetcode id=1054 lang=python3
#
# [1054] Distant Barcodes
#

# @lc code=start
from typing import Counter, List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counts = Counter(barcodes)
        
        barcodes.sort(key=lambda x: (-counts[x], x))
        
        n = len(barcodes)
        res = [0] * n
        res[::2] = barcodes[:(n + 1) // 2]
        res[1::2] = barcodes[(n + 1) // 2:]
        
        return res
# @lc code=end

