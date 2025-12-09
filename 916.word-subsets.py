#
# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#

# @lc code=start
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        from collections import Counter

        def merge_counters(c1: Counter, c2: Counter) -> Counter:
            for char in c2:
                c1[char] = max(c1[char], c2[char])
            return c1

        b_counter = Counter()
        for b in words2:
            b_counter = merge_counters(b_counter, Counter(b))

        result = []
        for a in words1:
            a_counter = Counter(a)
            if all(a_counter[char] >= b_counter[char] for char in b_counter):
                result.append(a)

        return result
# @lc code=end

