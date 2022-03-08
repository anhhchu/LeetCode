# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create new linked list with sentinel node
        head = ListNode()
        new_node = head
        # go through both lists and add the smaller node to the new list
        while list1 or list2:
            # only list2 left
            if not list1:
                node = list2
                list2 = list2.next
            # only list1 left
            elif not list2:
                node = list1
                list1 = list1.next
            # both lists left
            else: 
                if list1.val <= list2.val:
                    node = list1
                    list1 = list1.next
                else:
                    node = list2
                    list2 = list2.next
            # stitch the node to the new list
            new_node.next = node
            new_node = new_node.next
        
                    
        return head.next
                
                
        