class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def reConstructBinaryTree(self, pre, tin):
        if not pre:
            return None
        root = TreeNode(pre[0])
        index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre[1:index + 1], tin[0: index])
        root.right = self.reConstructBinaryTree(pre[index + 1:], tin[index + 1:])
        return root


def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)


S = Solution()
preorder(S.reConstructBinaryTree([1, 2, 3, 4, 5, 6, 7], [3, 2, 4, 1, 6, 5, 7]))
