class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_s = {} #hashmap for string s
        hash_t = {} #hashmap for string t

        for letter in s:
            if letter in hash_s:
                hash_s[letter]+= 1
            else:
                hash_s[letter] = 1
        
        for letter in t:
            if letter in hash_t:
                hash_t[letter]+= 1
            else:
                hash_t[letter] = 1
        
        return hash_s == hash_t