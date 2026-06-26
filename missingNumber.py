class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        h=0
        for i in range (len(nums)):
            if i!=nums[i]:
                h=1
                break
        if h==1:
            print(i)
        else:
            print(i+1)
