// 20 Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

function isValid(s: string): boolean {
  const stack = [];

  const left = '(';
  const right = ')';
  const middleLeft = '{';
  const middleRight = '}';
  const largeLeft = '[';
  const largeRight = ']';

  if (s.length <= 1) {
    return false;
  }

  if (s[0] === right || s[0] === middleRight || s[0] === largeRight) {
    return false;
  }

  for (let i = 0; i < s.length; i++) {
    if (s[i] === left || s[i] === middleLeft || s[i] === largeLeft) {
      stack.push(s[i]);
      continue;
    }

    const c = stack.pop();

    if (s[i] === right && c !== left) {
      return false;
    }

    if (s[i] === middleRight && c !== middleLeft) {
      return false;
    }

    if (s[i] === largeRight && c !== largeLeft) {
      return false;
    }
  }

  return stack.length === 0;
}
