"""

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""

"""使用一个hashtable 记录下p个元素的应该出现次数，然后用两个指针去遍历字符串
在此过程中，不能将在p中没有出现过的元素加入hashtable中
"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        left = right = 0
        count = len(p)
        dic = dict()
        for i in p:
            dic[i] = dic.get(i,0)+1
        while right < len(s):
            if s[right] in dic.keys():
                if dic[s[right]]>=1:
                    count = count - 1
                dic[s[right]] = dic[s[right]]-1
            right = right+1
            if count == 0 :
                res.append(left)
            if right - left == len(p):
                if s[left] in dic.keys():
                    if dic[s[left]]>=0:
                        count = count + 1
                    dic[s[left]]+=1
                left = left+1
        return res