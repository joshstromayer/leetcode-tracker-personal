# Problem 0058: Length Of Last Word
# Your solution:
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        str = s.split()
        for char in str[-1]:
            if char:
                count+=1
        return count