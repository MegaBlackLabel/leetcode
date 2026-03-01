#
# @lc app=leetcode id=3079 lang=python3
#
# [3079] Find the Sum of Encrypted Integers
#

# @lc code=start
from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
        def encrypt(x: int) -> int:
            max_digit = 0
            s = str(x)
            max_digit = int(max(s))
            length = len(s)
            
            encrypted_num = max_digit * (10**length - 1) // 9
            return encrypted_num

        return sum(encrypt(x) for x in nums)
# @lc code=end

