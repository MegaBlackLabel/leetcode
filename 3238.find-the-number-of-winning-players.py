#
# @lc app=leetcode id=3238 lang=python3
#
# [3238] Find the Number of Winning Players
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        player_counts = [defaultdict(int) for _ in range(n)]
    
        
        winners = set()
    
        for player, color in pick:
            player_counts[player][color] += 1
        
            if player_counts[player][color] > player:
                winners.add(player)
            
        return len(winners)
# @lc code=end

