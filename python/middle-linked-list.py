# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head
    
    head = [1,2,3,4,5]
    middleNode(head)