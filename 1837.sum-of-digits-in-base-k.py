#
# @lc app=leetcode id=1837 lang=python3
#
# [1837] Sum of Digits in Base K
#

# @lc code=start
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans=0
        while (n>=k):
            ans+=n%k
            n//=k
        return ans +n
# @lc code=end

