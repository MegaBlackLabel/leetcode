#
# @lc app=leetcode id=809 lang=python3
#
# [809] Expressive Words
#

# @lc code=start
from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def get_groups(word: str) -> List[tuple[str, int]]:
            groups = []
            prev_char = ''
            count = 0

            for char in word:
                if char == prev_char:
                    count += 1
                else:
                    if prev_char:
                        groups.append((prev_char, count))
                    prev_char = char
                    count = 1

            if prev_char:
                groups.append((prev_char, count))

            return groups

        s_groups = get_groups(s)
        expressive_count = 0

        for word in words:
            w_groups = get_groups(word)

            if len(s_groups) != len(w_groups):
                continue

            is_expressive = True
            for (s_char, s_count), (w_char, w_count) in zip(s_groups, w_groups):
                if s_char != w_char:
                    is_expressive = False
                    break
                if s_count < w_count or (s_count < 3 and s_count != w_count):
                    is_expressive = False
                    break

            if is_expressive:
                expressive_count += 1

        return expressive_count
# @lc code=end

