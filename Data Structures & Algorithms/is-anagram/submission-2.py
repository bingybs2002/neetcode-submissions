class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Length needs to be the same
        if len(s) != len(t):
            return False

        #Create an array of 26 elements
        count = [0] * 26

        # For each character in S, add it to array count.
        # For each character in T, minus it to array count.
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
            count[ord(t[i])-ord('a')] -= 1

        # All element in array should be 0
        for val in count:
            if val != 0: 
                return False

        return True