class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for a in nums:
            if a in hashmap:
                return True
            hashmap.add(a)
        return False
        