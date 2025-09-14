#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = []

        def backtrack(i: int, path: List[str]) -> None:
            if i == len(s):
                res.append("".join(path))
                return

            if s[i].isalpha():
                path.append(s[i].lower())
                backtrack(i + 1, path)
                path.pop()

                path.append(s[i].upper())
                backtrack(i + 1, path)
                path.pop()
            else:
                path.append(s[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
# @lc code=end

