class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [[-1,0]]
        n = len(temperatures)
        output = [0] * n
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prevtemp, prevIdx = stack.pop()
                output[prevIdx] = (i - prevIdx)
            stack.append([temp, i])
        return output
                


