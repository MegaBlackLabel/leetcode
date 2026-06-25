#
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#

# @lc code=start
from typing import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        char_counts = Counter(tiles)
        
        def backtrack() -> int:
            total_sequences = 0
            
            for char in char_counts:
                if char_counts[char] > 0:
                    char_counts[char] -= 1
                    
                    total_sequences += 1 + backtrack()
                    
                    char_counts[char] += 1
                    
            return total_sequences
            
        return backtrack()
# @lc code=end

