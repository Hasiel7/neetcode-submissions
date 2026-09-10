class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for c in s:
            if c.isalnum():
                string += c.lower()
        k = len(string) - 1
        i = 0

        while i <= k:
            if i == k:
                return True
            elif string[i] == string[k]:
                i += 1
                k -= 1
            else:
                return False
        return True