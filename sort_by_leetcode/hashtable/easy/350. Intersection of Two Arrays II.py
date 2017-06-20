"""

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""
"""使用两个字典记录下两个数组中元素出现的次数"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1,dic2 = dict(),dict()
        for num in nums1:
            dic1[num] = dic1.get(num,0) + 1
        for num in nums2:
            dic2[num] = dic2.get(num,0) + 1
        return [x for x in dic2 for j in range(min(dic1.get(x,0),dic2.get(x,0)))]

"""但是python内置了Counter类型数组，可以方便实现计数功能"""
import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1,c2 = collections.Counter(nums1),collections.Counter(nums2)
        return [i for i in c1.keys() for j in range(min([c1[i], c2[i]]))]