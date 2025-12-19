"""
Approach:
I created a LinkedList class that would keep track of its head by itself and have the ability to add
new listNodes by taking in a value and setting the new ListNode's pointer to be the current head. 

Issues:
LeetCode won't accept the answer, because I am supposed to use the LinkedList class in LeetCode rather
than make my own. 

Tests:
[2,4,3], [5,6,4] --> time limit exceeded
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class LinkedList(object):
    def __init__(self, head):
       self.head = head
    def add_node(self, val):
        new_node = ListNode(val, self.head)
        self.head = new_node


class Solution:
    def len(self, listNode):
        counter = 0
        current = listNode
        while current is not None:
            counter+=1
            current = current.next
        return counter
    def addTwoNumbers(self, l1, l2):
        total = 0
        firstL1 = l1
        firstL2 = l2
        for n in range(self.len(l1)):
            total+=firstL1.val*pow(10, n)
            firstL1 = firstL1.next
        for n in range(self.len(l2)):
            total+=firstL2.val*pow(10, n)
            firstL2 = firstL2.next

        output = LinkedList(total//10)
        total = (total-(total//10))/10

        for i in range(len(str(total))):
            output.add_node(total//10)
            total = (total-(total//10))/10

        return output



if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
    print(sol.addTwoNumbers())
