# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        first = None  # First misplaced node
        second = None  # Second misplaced node
        prev = None  # Keeps track of the previous node during traversal

        def inorder(node):
            nonlocal first, second, prev
            if not node:
                return

            inorder(node.left)  # Visit left subtree

            if prev and prev.val > node.val:
                if not first:
                    first = prev  # Mark the first violation
                second = node  # Mark the second violation
            prev = node  # Update `prev` to current node

            inorder(node.right)  # Visit right subtree

        inorder(root)  # Perform inorder traversal to identify swapped nodes

        # Swap the values of the two nodes
        if first and second:
            first.val, second.val = second.val, first.val