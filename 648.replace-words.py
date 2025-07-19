#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        root_set = set(dictionary)
        words = sentence.split()

        def find_root(word):
            for i in range(1, len(word) + 1):
                if word[:i] in root_set:
                    return word[:i]
            return word

        replaced_words = [find_root(word) for word in words]

        return ' '.join(replaced_words)
# @lc code=end

