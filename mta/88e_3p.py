class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # Start from the end of nums1 and nums2
        p1, p2, p = m - 1, n - 1, m + n - 1

        # Merge in reverse order
        while p2 >= 0:
            if p1>=0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
######################
            

        # a = 0
        # b = 0
        # while a < m+n and b<n:
        #     if nums1[a]>nums2[b] or nums1[a]==0:
        #         if nums1[a]==0:
        #             nums1[a]=nums2[b]
        #             b+=1
        #         else:
        #             tmp=nums1[a]
        #             nums1[a]=nums2[b]
        #             nums2[b]=tmp
        #     a+=1
        # return nums1
