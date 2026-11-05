def shiftZersToTheEnd(nums: list[int]) -> list[int]:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums

nums = [0, 2, 0, 0, 5, 0, 7]
print(shiftZersToTheEnd(nums))