// 2621. Sleep
// https://leetcode-cn.com/problems/sleep/

async function sleep(millis: number): Promise<void> {
  return new Promise((resolve) => {
    return setTimeout(resolve, millis);
  });
}

/**
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
