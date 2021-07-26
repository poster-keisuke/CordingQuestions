// 1. Two Sum
// https://leetcode.com/problems/two-sum/

function twoSum(nums: number[], target: number): number[] {
  const map = {};
  for (let i = 0; i < nums.length; i++) {
    if (target - nums[i] in map) {
      return [i, map[target - nums[i]]];
    }
    map[nums[i]] = i;
  }
  return [];
}

function twoSumBruteForce(nums: number[], target: number): number[] {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }

  return [];
}
