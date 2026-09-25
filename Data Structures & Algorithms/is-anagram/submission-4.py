class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        for char_1 in s:
            if char_1 in hash1:
                hash1[char_1] += 1
            else:
                hash1[char_1] = 1

        for char_2 in t:
            if char_2 in hash2:
                hash2[char_2] += 1
            else:
                hash2[char_2] = 1

        return hash1 == hash2
        