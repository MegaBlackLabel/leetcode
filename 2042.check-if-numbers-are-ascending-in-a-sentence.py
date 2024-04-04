#
# @lc app=leetcode id=2042 lang=python3
#
# [2042] Check if Numbers Are Ascending in a Sentence
#

# @lc code=start
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = 0

        for token in s.split():
            if token.isdigit():
                num = int(token)
                if num <= prev:
                    return False
                prev = num

        return True
# @lc code=end

