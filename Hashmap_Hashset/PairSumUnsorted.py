def pairSumUnsortedBruteForce(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def pairSumUnsorted(nums: list[int], target: int) -> list[int]:
    num_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in num_map:
            return [num_map[complement], i]

        num_map[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9
''''
(3 - (-1) = 4) - -1: 0
(3 - 3 = 0) - 3: 1
(3 - 4 = -1) - return the answer [-1 index from the map, current index) -> (0, 2)

'''
print(pairSumUnsortedBruteForce(nums, target))
print(pairSumUnsorted(nums, target))