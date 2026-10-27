class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hash_map = {}
        for i in arr:
            hash_map[i] = hash_map.get(i,0) + 1

        seen = set()
        for c in hash_map.values():
            if c in seen:
                return False
            seen.add(c)
        return True