"""
Approach:
Create a function that merges two given lists in ascending order by creating a dummy node and then 
adding onto the dummy node. Nodes are added by first checking if the values exist; if they do, they
are compared, and the smaller one is added onto the dummy node. If only one exists, it is automatically
added onto the dummy node. After none exist, the dummy node is returned. 

This process is repeated for every pair of lists in the "lists" list, in which the merged list of the 
first two lists is appended to "lists" and the two lists are deleted. Once only one list exists, the
final list is returned. If none exist, then an empty list is returned.

Time Complexity:  O(kN)
Space Complexity: O(1)

Issues:
An empty list is not accepted, because it doesn't match the required return type. Moreover, the answer
for tests are incorrect; 0s are added onto the front, and the last elements of some of the lists are
ignored. 

Tests:
[] --> [], expected return type is Optional[ListNode]
[[]] --> [], expected return type is Optional[ListNode]
[[1,2,4],[1,3,5],[3,6]] --> [0,0,1,1,2,3,3,5], correct answer: [1,1,2,3,3,4,5,6]
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
        return d1

    def mergeKLists(self, lists):
        while len(lists) >= 2:
            lists.append(self.mergeTwoLists(lists[0],lists[1]))
            lists.pop(0)
            lists.pop(0)
        if lists:
            return lists[0]
        else:
            return []



if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
