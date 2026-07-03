class Solution(object):
    def intersect(self, nums1, nums2):
        # ans = []
        # for i in range(len(nums2)):
        #     if nums2[i] in nums1:
        #         ans.append(nums2[i])
        #         nums1.remove(nums2[i])

        # return ans

        #USING HASH MAP
        freq = {}

        # Build frequency map
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        # Find intersection
        ans = []
        for num in nums2:
            if freq.get(num, 0) > 0:
                ans.append(num)
                freq[num] -= 1

        return ans

        

        