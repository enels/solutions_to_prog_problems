class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums = list()
        nums.extend(nums1)
        nums.extend(nums2)

        nums.sort()

        nums_len = len(nums)

        if nums_len % 2 == 1:
            mid_index = nums_len // 2
            mid = nums[mid_index]
            return mid
        else:
            mid_index1 = nums_len // 2
            mid_index2 = mid_index1 - 1
            mid = (nums[mid_index1] + nums[mid_index2]) / 2.0
            return mid