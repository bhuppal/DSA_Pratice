def setMatrixZerosInPlace(nums: list[list[int]]) -> None:
    print('before')
    for row in nums:
        print(' '.join(map(str, row)))

    m, n = len(nums), len(nums[0])
    first_row_has_zero = False
    for c in range(n):
        if nums[0][c] == 0:
            first_row_has_zero = True
            break

    first_col_has_zero = False
    for r in range(m):
        if nums[r][0] == 0:
            first_col_has_zero = True
            break

    for r in range(1, m):
        for c in range(1, n):
            if nums[r][c] == 0:
                nums[0][c] = 0
                nums[r][0] = 0

    for r in range(1, m):
        for c in range(1, n):
            if nums[0][c] == 0 or nums[r][0] == 0:
                nums[r][c] = 0

    if first_row_has_zero:
        for c in range(n):
            nums[0][c] = 0

    if first_col_has_zero:
        for r in range(m):
            nums[r][0] = 0

    print('after')
    for row in nums:
        print(' '.join(map(str,row)))
'''
[1, 0, 1]
[0, 0, 0]
[1, 0, 1]
'''


def setMatrixZeros(nums: list[list[int]]) -> None:
    if not nums or not nums[0]:
        return
    row_set = set()
    col_set = set()
    for r in range(len(nums)):
        for c in range(len(nums[0])):
            val = nums[r][c]
            if val == 0:
                row_set.add(r)
                col_set.add(c)

    for r in range(len(nums)):
        for c in range(len(nums[0])):
            if r in row_set or c in col_set:
                nums[r][c] = 0

    print('Bruteforce')
    for row in nums:
        print(' '.join(map(str, row)))

nums = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# setMatrixZeros(nums)
setMatrixZerosInPlace(nums)