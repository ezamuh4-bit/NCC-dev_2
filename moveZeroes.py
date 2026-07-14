class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=len(nums)
        while 0 in nums:
            nums.remove(0)
        nums.extend([0]*(s-len(nums)))
            
