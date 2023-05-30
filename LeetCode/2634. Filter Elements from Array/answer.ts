// 2634. Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
  const results: number[] = [];
  arr.forEach((item, index) => {
    if (fn(item, index)) {
      results.push(item);
    }
  });

  return results;
}
