class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        p=0
        q=n-1
        while p<=q:
            mid = (p+q)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                q=mid-1
            else:
                p=mid+1
        return -1
        