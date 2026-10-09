#
# @lc app=leetcode id=1292 lang=python3
#
# [1292] Maximum Side Length of a Square with Sum Less than or Equal to Threshold
#

# @lc code=start
class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j] 
                    + prefix[i][j + 1] 
                    + prefix[i + 1][j] 
                    - prefix[i][j]
                )
        
        ans = 0
        for i in range(m):
            for j in range(n):
                while (
                    i >= ans and j >= ans 
                    and (
                        prefix[i + 1][j + 1] 
                        - prefix[i - ans][j + 1] 
                        - prefix[i + 1][j - ans] 
                        + prefix[i - ans][j - ans]
                    ) <= threshold
                ):
                    ans += 1
                    
        return ans
# @lc code=end

