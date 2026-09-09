class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            org = "".join(sorted(word))
            if org not in anagrams:
                anagrams[org] = [word]
            else:
                anagrams[org].append(word)
        return list(anagrams.values())