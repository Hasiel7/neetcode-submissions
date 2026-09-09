class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stor = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in stor:
                return [stor.get(complement), i]
            stor[num] = i