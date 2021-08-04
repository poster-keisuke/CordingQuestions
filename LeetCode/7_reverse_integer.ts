// 7. Reverse Integer
// https://leetcode.com/problems/reverse-integer/

function reverse(x: number): number {
  let isNegative = false;

  if (x < 0) {
    isNegative = true;
  }

  let original = Math.abs(x);
  let num = 0;

  for (let i = 0; i < String(Math.abs(x)).length; i++) {
    num = num * 10 + (original % 10);
    original = Math.floor(original / 10);
  }

  if (Math.abs(num) >= 2 ** 31) return 0;

  if (isNegative) return -num;
  return num;
}

function reverse2(x: number): number {
  if (Math.abs(x) >= 2 ** 31) return 0;

  let factor = 1;
  if (x < 0) {
    factor = -1;
  }

  let original = Math.abs(x);
  let num = 0;

  while (0 < original) {
    num = num * 10 + (original % 10);
    original = Math.floor(original / 10);

    if (Math.abs(num) >= 2 ** 31) return 0;
  }

  return num * factor;
}
