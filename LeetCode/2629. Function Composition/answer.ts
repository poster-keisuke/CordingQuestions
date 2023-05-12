// 2629. Function Composition
// https://leetcode.com/problems/function-composition/description/

type F = (x: number) => number;

function solution(functions: F[]): F {
  return function (x) {
    if (functions.length === 0) return x;

    let input = x;
    for (let i = functions.length - 1; i >= 0; i--) {
      const cur = functions[i];
      input = cur(input);
    }
    return input;
  };
}
