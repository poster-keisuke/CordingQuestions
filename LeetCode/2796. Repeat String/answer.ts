// 2796. Repeat String
// https://leetcode.com/problems/repeat-string/

declare global {
  interface String {
    replicate(times: number): string;
  }
}

String.prototype.replicate = function (times: number) {
  let result = '';
  for (let i = 0; i < times; i++) {
    result += this;
  }

  return result;
};
