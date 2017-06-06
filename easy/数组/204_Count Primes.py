"""

Count the number of prime numbers less than a non-negative number, n.
统计素数的个数

"""

"""my solution 超时

"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        res = [1] * (n - 1)
        for i in range(2, n / 2 + 1):
            b = 2
            while b * i < n:
                res[b * i - 1] = 0
                b = b + 1

        return (sum(res) - 1)


"""fast solution 其实是一样的思想，但是解法巧妙，"""

class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        """循环的范围进行了缩小"""
        for i in range(2, int(n ** 0.5) + 1):
            """先判断是否已经变为false，同时从i*i开始进行遍历"""
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)