class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxOutput = 0
        #num is valid start if num - 1 exists in set
        for num in setNums:
            prev = num - 1
            if prev not in setNums:
                output = 1
                nextNum = num + 1
                while nextNum in setNums:
                    output += 1
                    nextNum += 1
                maxOutput = max(maxOutput, output)
        return maxOutput
    