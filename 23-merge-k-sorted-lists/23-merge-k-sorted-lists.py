# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # put all nums into a min heap
        # build an output list by popping element from min heap
        # O(NlogN) = (500*10^4)*log(500*10^4)
        minHeap = [] # O(N)
        for head in lists: #O(k)
            node = head
            while node: # O(500)
                heapq.heappush(minHeap, node.val) # O(logN)
                node = node.next
                
        #print(minHeap)
        head = ListNode(0)
        node = head
        
        while minHeap: # O(N)
            node.next = ListNode(heappop(minHeap))
            node = node.next 
            
        return head.next
        