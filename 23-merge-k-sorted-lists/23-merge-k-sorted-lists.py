# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    # compare k elements at each index of all lists using minHeap # O(k)
    # pop from minHeap O(logk)
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # create empty output linkedList with sentinel head node
        head = node = ListNode(0) 
        minHeap = []
        count = 0
        for lst in lists: # add first k elements into heap # O(k)
            count += 1
            if lst:
                # add  `lst.val` and `count` for comparison
                heapq.heappush(minHeap, (lst.val, count, lst)) 
        
        while minHeap: # O(N)
            count += 1
            val, _, current = heapq.heappop(minHeap) # O(logk)
            # add the current node to output list so we don't have to create a new node
            node.next = current 
            # add the next node to minHeap for the next iteration
            if current.next:
                heapq.heappush(minHeap, (current.next.val, count, current.next)) # O(logk)
            # remove the next pointer for current node
            current.next = None
            # update node 
            node = node.next
            
        return head.next
            
            
            
        
                
        