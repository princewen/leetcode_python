"""

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

"""

"""my solution
使用排列组合的知识，要注意除法的地方，j要乘1.0
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        min_step = n / 2 + n % 2
        max_step = n
        count = 0
        for i in range(min_step, max_step):
            n2 = max_step - i
            semi_count = 1
            for j in range(1, n2 + 1):
                semi_count *= ((i - j + 1) / (j * 1.0))
            count += semi_count

        return int(count + 1)


"""好的答案
这是一个斐波那契数列,首先到达n层的方法数，为到达n-1层和n-2层的方法数之和，依次类推，到达n-1层的方法数为到达n-2层和到达n-3层的方法数之和，
到达n-2层的方法数之和为到达n-3层和n-4层的方法数之和，依次类推。这些方法没有重复的部分，类似于一个斐波那契数列，可以举一些简单的例子来证明。
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = b = 1
        for i in range(1,n):
            a,b = b,a+b
        return b


