class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        s=Counter(nums)
        return max(s, key=s.get)
        
