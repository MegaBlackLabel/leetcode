/*
 * @lc app=leetcode id=1 lang=typescript
 *
 * [1] Two Sum
 */

// @lc code=start
function twoSum(nums: number[], target: number): number[] {
    // 辞書を作る
    let map = new Map<number, number>();
    // numsの要素を順番に見ていく
    for (let i = 0; i < nums.length; i++) {
        // targetからnums[i]を引いた値が辞書にあれば、そのインデックスと現在のインデックスを返す
        if (map.has(target - nums[i])) {
            return [map.get(target - nums[i])!, i];
        }
        // なければ、nums[i]とインデックスを辞書に追加する
        map.set(nums[i], i);
    }

    // 答えが見つからなければ空の配列を返す
    return [];
};

// @lc code=end

