class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights) - 1
        maxWater = 0
        i = 0
        while i < n:
            width = n - i
            minHeight = min(heights[i], heights[n])
            water = width * minHeight
            maxWater = max(maxWater, water)
            if heights[i] > heights[n]:
                n -= 1
            else:
                i += 1
        return maxWater