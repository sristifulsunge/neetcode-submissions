# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #using a hashset
        visited = set()
        dummy = head
        while dummy:
            if dummy in visited:
                return True
            visited.add(dummy)  
            dummy = dummy.next
        
        return False
        