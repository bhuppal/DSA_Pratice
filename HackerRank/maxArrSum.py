def getMaxArrSum(nums: list[int]) -> int:
    n = len(nums)
    left, right, total = 0, n - 1, 0
    left_max, right_max, total = 0, 0, 0

    while left <= right:
        if nums[left] < nums[right]:
            left_max = max(left_max, nums[left])
            total += left_max
            left += 1
        else:
            right_max = max(right_max, nums[right])
            total += right_max
            right -= 1
    return total



nums = [5, 1, 7, 1, 4]
print(getMaxArrSum(nums))

