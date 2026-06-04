# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:   
    def isSameTree(self, p, q):
        if p == q == None:
            return True
        elif not q:
            return False
        elif not p:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        #Explore
        #The idea is to check if a smaller tree exists in a larger tree
        #Can the subroot be none? If so do we return True or False
        #Brainstorm
        #Plan
        #Implement
        #Verify
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)