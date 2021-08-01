// 35. Search Insert Position
// https://leetcode.com/problems/search-insert-position/

function searchInsert(nums: number[], target: number): number {
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === target) {
      return i;
    }

    if (target < nums[i]) {
      return i;
    }
  }

  return nums.length;
}
