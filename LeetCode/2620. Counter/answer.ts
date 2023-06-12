// 2620. Counter
// https://leetcode-cn.com/problems/counter/

function createCounter(n: number): () => number {
  let num = n - 1;
  return function () {
    return (num += 1);
  };
}

/**
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
