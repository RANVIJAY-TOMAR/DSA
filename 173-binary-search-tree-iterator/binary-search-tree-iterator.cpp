class BSTIterator {
public:
    TreeNode* currentNode = nullptr;
    
    BSTIterator(TreeNode* root) {
        currentNode = root;
    }
    
    int next() {
        int result = -1;
        
        while (currentNode && result == -1) {
            if (!currentNode->left) {
                // Current node has no left subtree → visit immediately
                result = currentNode->val;
                currentNode = currentNode->right;
            } else {
                // Find inorder predecessor (rightmost node in left subtree)
                TreeNode* predecessor = currentNode->left;
                while (predecessor->right && predecessor->right != currentNode) {
                    predecessor = predecessor->right;
                }
                
                if (!predecessor->right) {
                    // Create temporary link to current node
                    predecessor->right = currentNode;
                    currentNode = currentNode->left;
                } else {
                    // Remove temporary link, then visit current node
                    predecessor->right = nullptr;
                    result = currentNode->val;
                    currentNode = currentNode->right;
                }
            }
        }
        return result;
    }
    
    bool hasNext() {
        return currentNode != nullptr;
    }
};