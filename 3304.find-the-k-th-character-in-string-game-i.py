#
# @lc app=leetcode id=3304 lang=python3
#
# [3304] Find the K-th Character in String Game I
#

# @lc code=start
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            new_part = ""
            for char in word:
                new_part += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            word += new_part
            
        return word[k - 1]
# @lc code=end

