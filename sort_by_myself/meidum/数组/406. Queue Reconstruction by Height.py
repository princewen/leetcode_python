"""

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


"""
"""按两个原则排序，按照身高的高低降序排序，同时按照前面人数升序排序，先排高的人，再排低的人"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []
        peopledict, height, res = {}, [], []
        for p in people:
            if p[0] in peopledict:
                peopledict[p[0]].append(p[1])
            else:
                peopledict[p[0]] = [p[1]]
                height.append(p[0])
        height.sort()
        for h in height[::-1]:
            peopledict[h].sort()
            for p in peopledict[h]:
                res.insert(p, [h, p])
        return res

