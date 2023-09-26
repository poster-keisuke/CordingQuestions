# 解説

## 最適解

### 概要

配列内の要素をソートし、2-pointers を利用して個数を算出する方法。
先にソートすることによって、不要な要素比較を省くことができるため、計算量は

- Time complexity: O(nlogn)
  - ソートの処理に依存している。
- Space complexity: O(1)

### 解答

```py
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort() # sort the vector nums
        count = 0 # variable to store the count
        left = 0 # variable to store the left
        right = len(nums)-1 # variable to store the right
        while(left < right): # loop until left is less than right
            if(nums[left] + nums[right] < target): # if nums[left] + nums[right] is less than target
                count += right-left # update the count
                left += 1 # increment the left
            else: # else
                right -= 1 # decrement the right
        return count # return the count
```

まず、配列自体をソートする。indexを返すことは不要なため、すべての組み合わせを検証できればOK
その後に、`left` と `right` の2つのポインターを定義し、`while` 文を実行する。

中身としては、`nums[left]` と `nums[right]` の値を比較し、`target` よりも小さければ、`right-left`（右インデックス - 左インデックス） をカウントする。
その後、`left` をインクリメントさせる。

上記比較がFalseであれば、 `right` をデクリメントさせ、`left` と `right` が交わる時点でループを終了し、リターンする。
