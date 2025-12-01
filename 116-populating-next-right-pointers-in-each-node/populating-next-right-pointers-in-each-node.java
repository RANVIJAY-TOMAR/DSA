class Solution {
    public Node connect(Node root) {
        if (root == null) return null;

        // leftmost is the first node of the current level
        Node leftmost = root;

        // since tree is perfect, if leftmost.left is null -> we're at leaves
        while (leftmost.left != null) {
            Node head = leftmost;

            // iterate across the current level using next pointers
            while (head != null) {
                // connect left -> right
                head.left.next = head.right;

                // connect right -> next.left (if next exists)
                if (head.next != null) {
                    head.right.next = head.next.left;
                }

                head = head.next;
            }

            // go down one level (leftmost child)
            leftmost = leftmost.left;
        }

        return root;
    }
}