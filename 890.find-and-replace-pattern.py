#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#

# @lc code=start
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def encode(word: str) -> str:
            mapping = {}
            code = []
            next_code = 0

            for char in word:
                if char not in mapping:
                    mapping[char] = str(next_code)
                    next_code += 1
                code.append(mapping[char])

            return ','.join(code)

        pattern_code = encode(pattern)
        result = []

        for word in words:
            if encode(word) == pattern_code:
                result.append(word)

        return result
# @lc code=end

