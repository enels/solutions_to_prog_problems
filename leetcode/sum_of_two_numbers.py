class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # get the length of the number
        len_nums = len(nums)
        for n in range(len_nums - 1):
            # next immediate number
            for m in range(n + 1, len_nums):
                # check for the sum
                if nums[n] + nums[m] == target:
                    return [n, m]
