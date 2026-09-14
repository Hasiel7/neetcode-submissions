class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0;
        seen = {}
        left = 0
        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            seen[char] = right
            maxLen = max(maxLen, right - left + 1)
        return maxLen    

            



# starting in the front, have a second pointer then move when a duplicate is found and count again, add char to map until duplicate char is found
