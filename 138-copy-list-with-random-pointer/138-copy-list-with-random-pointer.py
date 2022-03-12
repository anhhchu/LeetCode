"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {}
        copiedHead = Node(0)
        
        node = head
        copiedNode = copiedHead
        
        while node:
            if node and node not in hm:
                hm[node] = Node(node.val)            
            copiedNode.next = hm.get(node, None)
            copiedNode = copiedNode.next
            
            if node.random and node.random not in hm:
                hm[node.random] = Node(node.random.val)
            copiedNode.random = hm.get(node.random, None)
                
            node = node.next
            
            
        return copiedHead.next
            
            