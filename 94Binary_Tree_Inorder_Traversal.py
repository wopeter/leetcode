"""
Description
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def inorder(root, res):
            if root != None:
                inorder(root.left, res)
                res.append(root.val)
                inorder(root.right, res)
                
        inorder(root, res)
        return res
        
    def inorderTraversal2(self, root):
        