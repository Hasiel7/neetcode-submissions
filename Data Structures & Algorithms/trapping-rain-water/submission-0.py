class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxRight = [0] * n
        maxLeft = [0] * n
        water = 0

        maxLeft[0] = height[0]

        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        maxRight[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])

        for i in range(n):
            potential = min(maxRight[i], maxLeft[i])
            if potential - height[i] > 0:
                water += potential - height[i]

        return water
            
# for every i
# [0,2,0,3,1,0,1,3,2,1], max right = [0,2,2,3,3,3,3,3,3,3]
#                        max left  = [3,3,3,3,3,3,3,3,2,1]

#                        potential = [0,2,2,3,3,3,3,3,2,1]
#                        height    = [0,2,0,3,1,0,1,3,2,1]  
# potential - height = water