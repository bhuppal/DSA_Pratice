def twoSum(nums: list[int], target: int) -> list[int]:
    numSet = {}
    n = len(nums)
    for i in range(n):
        print(nums[i])
        complement = target - nums[i]
        if complement in numSet:
            return [numSet[complement], i]
        numSet[nums[i]] = i
    return []

nums = [3, 4, 5, 6]
target = 7

nums = [4, 5, 6]
target = 10

print(twoSum(nums, target))
