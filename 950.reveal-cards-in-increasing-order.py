#
# @lc app=leetcode id=950 lang=python3
#
# [950] Reveal Cards In Increasing Order
#

# @lc code=start
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        n = len(deck)
        index = list(range(n))
        result = [0] * n
        deck.sort()

        for card in deck:
            result[index.pop(0)] = card
            if index:
                index.append(index.pop(0))

        return result
# @lc code=end

