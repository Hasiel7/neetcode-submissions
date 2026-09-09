class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            org = "".join(sorted(word))
            anagrams[org].append(word)
        return list(anagrams.values())