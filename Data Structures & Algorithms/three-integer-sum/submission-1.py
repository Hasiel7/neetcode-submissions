class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums = sorted(nums)
        for i, num in enumerate(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums == 0:
                    output.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sums > 0:
                    k -= 1
                else:
                    j += 1
        return [list(x) for x in output]   




#                           i  j         k
#[-1,0,1,2,-1,-4] becomes [-4,-1,-1,0,1,2]

#have two pointers, create a third which satifies the sum == 0:, see if exists, if does
#put 3 values into group