class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        slide = set()

        for i in range(len(nums)):

            if nums[i] in slide:
                return True

            slide.add(nums[i])

            if len(slide) > k:
                slide.remove(nums[i - k])
        return False