class Solution(object):
    def arrayPairSum(self, nums):
        nums=nums.sort()
        maxarr=[]
        i=0
        while i<len(nums):
            maxarr.append(min(nums[i],nums[i+1]))
            i+=2
        return sum(maxarr)