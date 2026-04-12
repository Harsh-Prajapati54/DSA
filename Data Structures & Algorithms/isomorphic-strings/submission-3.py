
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
    #    len(set(zip(s, t))) it maps each caracter of s to t 
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
