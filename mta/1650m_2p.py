"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        tmpq = q
        tmpp = p
        while tmpq!=tmpp:
            tmpp = tmpp.parent if tmpp else q
            tmpq = tmpq.parent if tmpq else p
        return tmpp
