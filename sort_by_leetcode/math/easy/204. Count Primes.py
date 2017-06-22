"""

Description:

Count the number of prime numbers less than a non-negative number, n.

"""

"""统计比n小的质数有多少，首先设置一个数组，全部质为true，然后遍历2-sqrt（n）的数，把他们的倍数所在的数组位置
置为True这里为了避免重复，从i*i的位置开始，而不是从i*2的位置开始，因为i*2，i*3，i*n-1其实已经置为false了
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2,int(math.sqrt(n)) + 1):
            res[i*i:n:i] = [False] * len(res[i*i:n:i])
        return sum(res)