// 2665. Counter II
// https://leetcode.com/problems/counter-ii/description/

type ReturnObj = {
  increment: () => number;
  decrement: () => number;
  reset: () => number;
};

function createCounter(init: number): ReturnObj {
  const initial = init;
  return {
    increment: () => (init += 1),
    decrement: () => (init -= 1),
    reset: () => (init = initial),
  };
}

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
