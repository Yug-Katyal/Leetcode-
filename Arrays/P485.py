class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        streak = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
                streak = max(streak,count)

            else:
                count = 0

        return streak