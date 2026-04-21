# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode | None = None) -> TreeNode | None:
        if root is None:
            return None

        tree_queue = deque([root])
        while tree_queue:
            current_node = tree_queue.popleft()
            # Invert 2 nodes: left and right
            current_node.left, current_node.right = current_node.right, current_node.left
            if current_node.left:
                tree_queue.append(current_node.left)
            if current_node.right:
                tree_queue.append(current_node.right)
        return root
        