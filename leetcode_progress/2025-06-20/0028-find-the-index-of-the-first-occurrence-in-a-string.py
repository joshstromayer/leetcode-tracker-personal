# Problem 0028: Find The Index Of The First Occurrence In A String
# Your solution:
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        k=0
        i=0
        while i < len(haystack):
            if haystack[i] == needle[k]:
                k+=1
                if k == len(needle):
                    return i-k+1
            else: 
                i = i - k
                k = 0
            i += 1
        return -1

