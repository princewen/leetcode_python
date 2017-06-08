"""

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

"""

"""
my solution
用两个字典保存字母出现的次数，最后判断两个字典是否相同
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        for i in s:
            dic1[i] = dic1.get(i,0)+1
        for i in t:
            dic2[i] = dic2.get(i,0)+1
        return dic1 == dic2