class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            sort = "".join(sorted(word))
            if sort not in seen:
                seen[sort] = [word]
            else:
                seen[sort].append(word)
        return list(seen.values())