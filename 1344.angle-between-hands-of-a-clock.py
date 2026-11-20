#
# @lc app=leetcode id=1344 lang=python3
#
# [1344] Angle Between Hands of a Clock
#

# @lc code=start
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = minutes * 6
        
        # 時針の角度（1時間あたり30度 + 1分あたり0.5度）
        # 12時は0時として計算するため % 12 を使用
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        
        # 2つの針の角度の差
        diff = abs(hour_angle - minute_angle)
        
        # 小さい方の角度（180度以下）を返す
        return min(diff, 360 - diff)
# @lc code=end

