"""

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

"""

"""寻找可以形成的最大的水塘，这里的题目我理解有误，看到解答发现，只要取两头的最小值即可，不需要考虑中间的地方，所以用前后两个指针遍历数组"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return maxArea


