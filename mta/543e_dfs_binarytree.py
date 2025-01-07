# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.dm = 0

        def dfs(node):
            if not node: return 0
            right = dfs(node.right)
            left = dfs(node.left)
            self.dm = max(self.dm, right + left)

            return max(right,left)+1

        dfs(root)
        return self.dm

        # # stack = []
        # def trav(node, stack):
        #     if node: stack.append(node)
        #     else: return len(stack)
        #     return max(trav(node.left, stack), trav(node.right, stack))-1

        # return trav(root,[])
            
