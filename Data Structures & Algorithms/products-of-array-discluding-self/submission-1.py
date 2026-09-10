class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            # store prefix in output[i], then update prefix
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            # multiply output[i] by suffix, then update suffix
            output[i] *= suffix
            suffix *= nums[i]

        return output