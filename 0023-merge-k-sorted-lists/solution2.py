"""
Approach:
First, I fixed the return type issue for empty lists by returning None instead of []. Next, I returned
the next node after the dummy node in the mergeTwoLists() function to ensure that the default 0 that
the dummy node was set to was not included in the final result.

Time Complexity:  O(kN)
Space Complexity: O(1)

Issues:
The last element of certain lists is omitted. 

Tests:
[] --> []
[[]] --> []
[[1,2,4],[1,3,5],[3,6]] --> [1,1,2,3,3,5], correct answer: [1,1,2,3,3,4,5,6]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeTwoLists(self, l1, l2):
        d1 = ListNode(0)
        curr = d1
        while l1.next and l2.next:
            if l1.val <= l2.val: 
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next

        while l1.next:
            curr.next = l1
            curr = curr.next
            l1 = l1.next

        while l2.next:
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
