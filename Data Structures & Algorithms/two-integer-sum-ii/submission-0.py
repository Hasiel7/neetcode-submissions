# sorted in non decreasing order
# index 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n = len(numbers) - 1
        while i < n:
            sum = numbers[i] + numbers[n]
            if sum == target:
                return [i + 1, n + 1]
            elif sum < target:
                i += 1
            else:
                n -= 1
        return []


# start at front and back, for every number i, check n - 1 until i 
# index 1 < index 2
