// Palindrome Number
// https://leetcode.com/problems/palindrome-number/

function isPalindrome(x: number): boolean {
  if (String(x)[0] === '-') return false;

  for (let i = 0; i < String(x).length; i++) {
    if (String(x)[i] !== String(x)[String(x).length - i - 1]) {
      return false;
    }
  }

  return true;
}
