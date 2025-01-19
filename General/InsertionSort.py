import random


def insertion_sort(nums):
    for i in range(len(nums)):
        for j in range(0, i):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


nums = [random.randint(0, 1000) for i in range(10)]
print(insertion_sort(nums))
