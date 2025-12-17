"""
Approach:
I added a head to the ListNode class so I can keep track of the first ListNode. From there, I tried 
to convert the output list into a linked list by making new ListNodes for each ListNode's "next" 
attribute. 

Issues:
The code uses far too much space and time for computations. In addition, the ListNode class is still
not functional.

Tests:
[2,4,3], [5,6,4] --> memory limit exceeded
"""

class ListNode(object):
    def __init__(self, val=0, next=None, head=0):
       self.val = val
       self.next = next
       self.head = head
    

class Solution:
    def len(self, listNode):
        counter = 0
        current = listNode
        while current is not None:
            counter+=1
            current = current.next
        return counter
    
    def addTwoNumbers(self, l1, l2):
        output = 0
        firstL1 = l1
        firstL2 = l2
        for n in range(self.len(l1)):
            output+=firstL1.val*pow(10, n)
            firstL1 = firstL1.next
        for n in range(self.len(l2)):
            output+=firstL2.val*pow(10, n)
            firstL2 = firstL2.next

        output = str(output)
        new = []
        for item in output:
            new.append(int(item))
        new.reverse()
        
        final = ListNode()
        head = final
        for index, value in enumerate(new):
            if index < len(new)-1:
                final.val = int(value)
                final.next = ListNode(new[index+1])
                final = final.next
            else:
                final.val = int(value)
                final.next = head
        final = final.next

        return final



if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
    print(sol.addTwoNumbers([2,4,3], [5,6,4]))
