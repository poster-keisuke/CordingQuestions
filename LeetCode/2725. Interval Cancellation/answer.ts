// 2725. Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

function cancellable(fn: Function, args: any[], t: number): Function {
  let timerId;
  let time = 0;
  let result = [];

  function executeFn() {
    let returnedValue = fn.apply(null, args);
    result.push({ time: time, returned: returnedValue });
    time += t;
  }

  function cancelFn() {
    clearInterval(timerId);
  }

  executeFn();
  timerId = setInterval(executeFn, t);

  return cancelFn;
}

/**
 *  const result = []
 *
 *  const fn = (x) => x * 2
 *  const args = [4], t = 20, cancelT = 110
 *
 *  const log = (...argsArr) => {
 *      result.push(fn(...argsArr))
 *  }
 *
 *  const cancel = cancellable(fn, args, t);
 *
 *  setTimeout(() => {
 *     cancel()
 *     console.log(result) // [
 *                         //      {"time":0,"returned":8},
 *                         //      {"time":20,"returned":8},
 *                         //      {"time":40,"returned":8},
 *                         //      {"time":60,"returned":8},
 *                         //      {"time":80,"returned":8},
 *                         //      {"time":100,"returned":8}
 *                         //  ]
 *  }, cancelT)
 */
