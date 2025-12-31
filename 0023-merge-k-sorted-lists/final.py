"""
Approach:
I changed the conditionals in mergeTwoLists() from checking if l1.next/l2.next exists to whether l1/l2 
exists, because l1 = l1.next still works even if l1.next = None, and this method ensures the last 
element in the list is not left out.

Time Complexity:  O(kN)
Space Complexity: O(1)

Tests:
[[1,2,4],[1,3,5],[3,6]] --> [1,1,2,3,3,4,5,6]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeTwoLists(self, l1, l2):
        d1 = ListNode(0)
        curr = d1
        while l1 and l2:
            if l1.val <= l2.val: 
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next

        while l1:
            curr.next = l1
            curr = curr.next
            l1 = l1.next

        while l2:
            curr.next = l2
            curr = curr.next
            l2 = l2.next
        
        return d1.next

    def mergeKLists(self, lists):
        while len(lists) >= 2:
            lists.append(self.mergeTwoLists(lists[0],lists[1]))
            lists.pop(0)
            lists.pop(0)
        if lists:
            return lists[0]
        else:
            return None


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
