class Solution(object):
    def intersection(self, nums1, nums2):
       seen = set(nums1)
       ans = []
       for i in range(len(nums2)):
            if nums2[i] in seen:
                ans.append(nums2[i])
            
       return list(set(ans))
        