class Solution(object):
    def moveZeroes(self, nums):

        insert = 0
        for i in range (len(nums)):
            if nums[i] !=0:
                nums[insert] = nums[i]
                insert +=1
        for j in range(insert,len(nums)):
            nums[j] = 0
            
                
        