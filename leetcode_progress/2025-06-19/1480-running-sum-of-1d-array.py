# Problem 1480: Running Sum Of 1D Array
# Your solution:
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = []
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            runningSum.append(summ)
        return runningSum

