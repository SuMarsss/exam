class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size1, size2 = len(nums1), len(nums2)
        l1,r1, l2,r2 = 0, size1-1, 0, size2-1
        li = [l1,r1, l2,r2]
        min()