#
# @lc app=leetcode id=3318 lang=python3
#
# [3318] Find X-Sum of All K-Long Subarrays I
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        
        # 各k-longサブ配列をスライドしながら処理
        for i in range(n - k + 1):
            subarray = nums[i:i+k]
            counts = Counter(subarray)
            
            # 頻度(降順)、値(降順)でソート
            sorted_counts = sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)
            
            # 上位x個の頻度要素を取得
            top_x = sorted_counts[:x]
            
            # X-Sumを計算: 要素値 * 頻度
            current_sum = sum(val * freq for val, freq in top_x)
            res.append(current_sum)
            
        return res
# @lc code=end

