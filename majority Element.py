class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=Counter(nums)
        for i in m:
            if m[i]>=len(nums)/2:
                return i
