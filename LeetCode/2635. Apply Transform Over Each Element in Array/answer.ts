// 2635. Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/description/

function map(arr: number[], fn: (n: number, i: number) => number): number[] {
  const results: number[] = [];
  for (let i = 0; i < arr.length; i++) {
    results.push(fn(arr[i], i));
  }
  return results;
}
