"""

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        new_digits = []
        extra = 1
        for i in range(len(digits)-1,-1,-1):
            new_digits.append((digits[i]+extra)%10)
            extra = (digits[i]+extra)/10
        if extra == 1:
            new_digits.append((extra))
        length = len(new_digits)
        for i in range(len(new_digits)/2):
            new_digits[i],new_digits[length-i-1] = new_digits[length-i-1],new_digits[i]
        return new_digits


"""other solutions"""

def plusOne(digits):
    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]