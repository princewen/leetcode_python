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
"""利用hashtable将每个字母出现的次数记录下来，最长的回文数可以由三部分组成：
1、出现次数为偶数的，总长度增加其出现次数。2、出现次数为奇数，但是大于1次的，此时总长度增加其出现次数-1次。3、只要有出现次数为奇数的元素，总长度再加1
python中collecitons的Counter数据结构其实就是遍历数组形成一个hashtable并对各元素出现次数进行计数，使用非常方便
"""
import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = collections.Counter(s)
        return sum([t[x] for x in t if t[x] %2==0]) + sum([t[x]-1 for x in t if t[x] > 1 and t[x]%2==1])+max([1 for x in t if t[x]%2==1] or [0])