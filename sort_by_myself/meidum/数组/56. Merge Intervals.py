"""

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

"""
"""
my solution:先按照第一维排序，随后遍历数组，如果下一个元素的start小于前一个元素的end，说明两个需要合并，由于按照
第一维排序了，所以此时更新第二维为二者的较大值，如果下一个元素的start大于前一个元素的end，直接执行append操作
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x.start)
        res = [intervals[0]]
        for t in intervals[1:]:
            if t.start <= res[-1].end:
                res[-1].end = max(res[-1].end, t.end)
            else:
                res.append(t)
        return res
