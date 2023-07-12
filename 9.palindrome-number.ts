/*
 * @lc app=leetcode id=9 lang=typescript
 *
 * [9] Palindrome Number
 */

// @lc code=start
function isPalindrome(x: number): boolean {
    // check if negative
    if (x < 0) {
        // return false for negative numbers
        return false;
    }

    // store original number
    const original = x;

    // initialize reversed number
    let reversed = 0;

    // loop until num becomes zero
    while (x > 0) {
        // get last digit of num
        const lastDigit = x % 10;

        // add last digit to reversed number
        reversed = reversed * 10 + lastDigit;

        // remove last digit from num
        x = Math.floor(x / 10);
    }

    // check if original and reversed are equal
    return original === reversed;


};
// @lc code=end

