# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #FI-Get the path from the root to both nodes as a list and then traverse the list
        #backwards till you find a common number 
        #SI - keep a running list of the direct predecessor through the helper function and then when you find one of the nodes
        #stop changing it. When you find the second node value 
        if not root or not p or not q:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        