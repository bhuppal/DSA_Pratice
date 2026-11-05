def pairSumSortedBruteForce(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def pairSumSorted(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    left, right = 0, n - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []

nums = [-5, -2, 3, 4, 6]
target = 7
print(pairSumSortedBruteForce(nums, target))
print(pairSumSorted(nums, target))