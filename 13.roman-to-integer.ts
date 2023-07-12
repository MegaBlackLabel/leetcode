/*
 * @lc app=leetcode id=13 lang=typescript
 *
 * [13] Roman to Integer
 */




// @lc code=start
function romanToInt(s: string): number {

    const romanMap: { [key: string]: number } = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    };

    // 結果を格納する変数
    let result = 0;

    // 文字列の長さ
    let length = s.length;

    // 文字列を左から右へ走査するループ
    for (let i = 0; i < length; i++) {

        // 現在の文字と次の文字を取得
        let current = s[i];
        let next = s[i + 1];

        // 現在の文字と次の文字がマッピングに存在するかチェック
        if (romanMap[current] && romanMap[next]) {

            // 現在の文字が次の文字より小さい場合は引く
            if (romanMap[current] < romanMap[next]) {
                result -= romanMap[current];
            }

            // 現在の文字が次の文字以上である場合は足す
            else {
                result += romanMap[current];
            }
        }

        // 現在の文字だけマッピングに存在する場合は足す
        else if (romanMap[current]) {
            result += romanMap[current];
        }

        // マッピングに存在しない場合はエラーを返す
        else {
            return -1;
        }
    }

    // 結果を返す
    return result;
};
// @lc code=end


