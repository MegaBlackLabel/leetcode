#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        
        dp = {}
        max_chain_len = 1
        
        for word in words:
            current_longest = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    current_longest = max(current_longest, dp[predecessor] + 1)

            dp[word] = current_longest
            max_chain_len = max(max_chain_len, current_longest)
            
        return max_chain_len
# @lc code=end

