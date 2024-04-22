
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []

        def inorder(node: Optional[TreeNode]):
            if node is None:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        inorder(root)

        sortedNodes = sorted(nodes, key=lambda x: x.val)

        for i in range(len(nodes)):
            if nodes[i] != sortedNodes[i]:
                nodes[i].val, sortedNodes[i].val = sortedNodes[i].val, nodes[i].val
                break
