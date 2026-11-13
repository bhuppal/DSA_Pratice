def longestConsecutiveSequence(nums: list[int]) -> int:
    hash_set = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in hash_set:
            current_length = 0
            while (n + current_length) in hash_set:
                current_length += 1

            longest = max(current_length, longest)
    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutiveSequence(nums))
