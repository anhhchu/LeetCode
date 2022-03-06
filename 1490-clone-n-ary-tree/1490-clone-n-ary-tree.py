"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        node = Node(root.val)
            
        children = []
        if root.children:
            for childNode in root.children:
                child = self.cloneTree(childNode)
                children.append(child)
                
        node.children = children
        return node
                
                
            
            
            
            
            
        
    
    
            