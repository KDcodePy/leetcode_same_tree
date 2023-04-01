class Treenode:
    def __init__(self, val=0, left= None, right= None):
        self.val = val
        self.left = left 
        self.right = right

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class Solution:
    def __init__(p: Optional[Treenode], q: Optional[Treenode]) -> bool:

        # recursion approach
        # check p and q values
        if p and q:
            # return triple bool current, left, right 
            return p.val == q.val and self.isSameTree(p.left,q.right) and self.isSameTree(p.right,q.right)
        
        # if p and q have the same value it will return the same id 
        return p is q