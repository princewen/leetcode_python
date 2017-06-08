"""

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

"""

"""my solution"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1 = set(nums1)
        return [x for x in set(nums2) if x in nums1]

"""other solution
直接用set的基本操作：
>>> x = set("jihite")
>>> y = set(['d', 'i', 'm', 'i', 't', 'e'])
>>> x       #把字符串转化为set，去重了
set(['i', 'h', 'j', 'e', 't'])
>>> y
set(['i', 'e', 'm', 'd', 't'])
>>> x & y   #交
set(['i', 'e', 't'])
>>> x | y   #并
set(['e', 'd', 'i', 'h', 'j', 'm', 't'])
>>> x - y   #差
set(['h', 'j'])
>>> y - x
set(['m', 'd'])
>>> x ^ y   #对称差：x和y的交集减去并集
set(['d', 'h', 'j', 'm'])

"""

def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1=set(nums1)
    nums2=set(nums2)
    return list(nums1&nums2)