"""

题目描述有问题
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index-1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s