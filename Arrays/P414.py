class Solution(object):
    def thirdMax(self, nums):
        unique = sorted(set(nums))

        if len(unique) >= 3:
            return unique[-3]
        return unique[-1]