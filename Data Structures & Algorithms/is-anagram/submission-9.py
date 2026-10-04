class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        a=[]
        b=[]
        for i in range(0, len(s)):
            a.append(s[i])
            b.append(t[i])
        a.sort()
        b.sort()
        if(a != b):
            return False
        return True