class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in tracker:
                return [tracker.get(complement), i]
            else:
                tracker[num] = i
        return []