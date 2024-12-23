# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Dictionary to map column indices to node values
        column_table = {}

        # Queue for BFS traversal
        queue = [(root, 0)]  # Each element is (node, column_index)

        while queue:
            # Pop the front of the queue (FIFO behavior)
            node, column = queue.pop(0)

            if node:
                # Add the node's value to the column_table
                if column not in column_table:
                    column_table[column] = []
                column_table[column].append(node.val)

                # Add left and right children to the queue with their respective column indices
                if node.left:
                    queue.append((node.left, column - 1))
                if node.right:
                    queue.append((node.right, column + 1))

        # Sort columns by their index
        sorted_columns = sorted(column_table.keys())

        # Return the values in sorted column order
        return [column_table[col] for col in sorted_columns]
