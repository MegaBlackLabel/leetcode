#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#

# @lc code=start
from typing import List
from collections import defaultdict
from bisect import bisect_right

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        char_indices = defaultdict(list)

        for i, char in enumerate(s):
            char_indices[char].append(i)

        result = 0

        for word in words:
            prev_index = -1
            found = True

            for char in word:
                if char not in char_indices:
                    found = False
                    break

                indices = char_indices[char]
                pos = bisect_right(indices, prev_index)

                if pos == len(indices):
                    found = False
                    break

                prev_index = indices[pos]

            if found:
                result += 1

        return result
# @lc code=end

