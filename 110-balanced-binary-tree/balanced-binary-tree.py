class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(node):
            if not node:
                return 0

            leftHeight = checkHeight(node.left)
            if leftHeight == -1:
                return -1

            rightHeight = checkHeight(node.right)
            if rightHeight == -1:
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1

            return max(leftHeight, rightHeight) + 1

        return checkHeight(root) != -1