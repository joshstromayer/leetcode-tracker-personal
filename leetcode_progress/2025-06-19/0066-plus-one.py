# Problem 0066: Plus One
# Your solution:
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_digits = []
        for i in range(len(digits)):
            str_digits.append(str(digits[i]))

        inte = "".join(str_digits)
        inte = int(inte)
        inte +=1

        result = []
        for i in str(inte):
            result.append(int(i))
        return result
        

