def tripleSumBruteForce(nums: list[int]) -> list[list[int]]:
    triplets = set()
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    triplets.add(triplet)
    return [list(triplet) for triplet in triplets]


def tripleSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    triplets = []
    print(nums)
    for i in range(len(nums)):

        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        pairs = pair_sum(nums, i + 1, -nums[i])
        for pair in pairs:
            print(pair)
            triplets.append([nums[i]] + pair)

    return triplets



def pair_sum(nums: list[int], start: int, target: int) -> list[int]:
    n = len(nums)
    pairs = []
    left, right = start, n - 1
    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            pair = [nums[left], nums[right]]
            print(pair)
            pairs.append(pair)
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif total < target:
            left += 1
        else:
            right -= 1

    return pairs








nums = [0, -1, 2, -3, 1]
print(tripleSumBruteForce(nums))
print(tripleSum(nums))