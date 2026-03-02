"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
# Right so this problem can be thought of as a recursive algorithm comparing the elements of a list.
# Meaning, we will compare elements from the two lists recurively, until one is empty.
# So, comparing the both tops of the list, whichever is smaller, is appended to the solution_list, and poped on it's list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        if not list1:
            return list2
        
        elif not list2:
            return list1
        
        else:
            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1

            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2

