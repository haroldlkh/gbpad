# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or root == p or root == q: return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right: return root

        return left if left else right


        # p_path = []
        # tmp = root
        # while tmp != p:
        #     p_path.append(tmp)
        #     if p.val > tmp.val:
        #         tmp = tmp.left
        #     else: tmp = tmp.right
        # p_path.append(tmp)

        # tmp = root
        # depth = 0
        # while tmp!=q:
        #     depth+=1
        #     if depth > len(p_path)-1: return p_path[-1]

        #     if q.val > tmp.val:
        #         tmp = tmp.left
        #     else: tmp = tmp.right

        #     if tmp != p_path[depth]: return p_path[depth-1]

        # return tmp
