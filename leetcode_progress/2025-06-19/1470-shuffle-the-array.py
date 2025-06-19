# Problem 1470: Shuffle The Array
# Your solution:
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        nums1 = nums[0:n]
        nums2 = nums[n:]
        listnum = []
        for i in range(n):
            listnum.append(nums1[i])
            listnum.append(nums2[i])
        return listnum

