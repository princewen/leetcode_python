"""

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

"""

"""
my solution：结果分为三部分，计数数量为正数的，随后计数为单数的-1，最后，如果有单数元素存在，长度肯定可以加1
这里注意一个testcase "ccc"，应该返回3，瑞后的max要注意，只要有计数为单数的字符，都要加上1，而不是只有计数为1的才行

"""

import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = collections.Counter(s)
        return sum([t[x] for x in t if t[x] % 2 == 0]) + sum([t[x] - 1 for x in t if  t[x] % 2 == 1]) + max(
            [1 for x in t if t[x] % 2 == 1] or [0])
