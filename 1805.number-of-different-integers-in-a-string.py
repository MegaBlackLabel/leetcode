#
# @lc app=leetcode id=1805 lang=python3
#
# [1805] Number of Different Integers in a String
#

# @lc code=start
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = list(word)

        for i in range(len(word)):
            if word[i] in 'abcdefghijklmnopqrstuvwxyz':
                word[i] = ' '

        arr = ''.join(word)
        res = arr.split()
        res = [int(i) for i in res]

        return len(set(res))
# @lc code=end

