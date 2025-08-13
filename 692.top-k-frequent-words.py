#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        count = Counter(words)
        sorted_words = sorted(count.keys(), key=lambda x: (-count[x], x))

        return sorted_words[:k]
# @lc code=end

