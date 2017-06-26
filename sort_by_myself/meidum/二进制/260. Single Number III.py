"""

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

"""
"""既然是两个数出现了一次，那么我们可以将这些数分为两组，每一组的问题就转化为了只有一个数出现一次的问题
那么怎么分组呢，我们首先对所有的数进行按位异或，剩下的结果就是我们的两个目标值的异或结果，从右数第一个1就是
两个数最低的一个不同的位，我们就按照这位进行分组，假设结果是1101，我们要的分组值是0001，然后根据按位与就可以根据
最后一位将数组分为两部分，每一部分各包含了一个我们的目标值
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor = xor ^ num
        sep = xor & ~(xor - 1)
        num1 = num2 = 0
        for num in nums:
            if num & sep > 0:
                num1 ^= num
            else:
                num2 ^=num
        return [num1,num2]