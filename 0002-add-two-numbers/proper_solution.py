"""
NOTE: I did not write this code

Approach:
Create a dummy head for the linked list, initialize a current object to represent the current 
ListNode, and create a carry variable. While the value of the given linked lists (l1, l2) are 
not None or there is the carry variable is not 0, take the values of the first value of the linked
list. Add them and represent its remainder as sum_val and its quotient as carry. Create a new 
ListNode for the next iteration, and then advance the given linked lists. Finally, return the 
head of the linked list (skipping the dummy head).

Time Complexity:  O(max(n,m))
Space Complexity: O(max(n,m))
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # 1. Initialize a dummy head for the result list
        dummy_head = ListNode()
        current = dummy_head
        carry = 0
        
        # 2. Iterate while there are nodes in either list OR a carry exists
        while l1 is not None or l2 is not None or carry != 0:
            
            # Get the values, treating None as 0
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # 3. Sum the values and the carry
            sum_val = val1 + val2 + carry
            
            # 4. New digit for the result list (the remainder)
            new_digit = sum_val % 10
            
            # 5. New carry for the next iteration (the quotient)
            carry = sum_val // 10
            
            # 6. Append the new node and advance the current pointer
            current.next = ListNode(new_digit)
            current = current.next
            
            # 7. Advance input list pointers
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        # 8. Return the actual head of the list (skipping the dummy node)
        return dummy_head.next


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
