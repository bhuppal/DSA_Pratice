# (j - i) * min(h[i], minofheight)

def largestContainerBruteForce(heights: list[int]) -> int:
    n = len(heights)
    maxWater = 0
    for i in range(n):
        for j in range(i + 1, n):
            water = min(heights[i], heights[j]) * (j - i)
            maxWater = max(maxWater, water)
    return maxWater

def largestContainer(heights: list[int]) -> int:
    n = len(heights)
    maxWater = 0
    left, right = 0, n - 1
    while left < right:
        water = min(heights[left], heights[right]) * (right - left)
        maxWater = max(maxWater, water)

        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    return maxWater

heights = [2, 7, 8, 3, 7, 6]
print(largestContainerBruteForce(heights))
print(largestContainer(heights))