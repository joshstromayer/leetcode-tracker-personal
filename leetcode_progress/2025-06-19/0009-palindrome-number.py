# Problem 0009: Palindrome Number
# Your solution:
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = ''
        x = str(x)
        for i in reversed(range(len(x))):
            y += x[i]
        if x == y:
            return True
        else:
            return False
            
d

