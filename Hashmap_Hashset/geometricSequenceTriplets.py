from collections import Counter

def geometricSequenceTriplets(nums: list[int],r: int) -> int:
    right = {}
    for x in nums:
        right[x] = right.get(x,0) + 1

    left = {}
    total = 0

    # {2: 2, 1: 1, 4: 1, 8: 2}
    for x in nums:
        right[x] -= 1
        if x % r == 0:
            total += left.get(x // r, 0) * right.get(x * r, 0)
        left[x] = left.get(x, 0) + 1
    return total



nums = [2, 1, 2, 4, 8, 8]
r = 2

print(geometricSequenceTriplets(nums, r))
