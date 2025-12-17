"""
Approach:
I added a length function that can take in a listNode and output its length by creating a counter
and having it increase by one until the function reaches the end of the listNode. 

I also implemented the ListNode class given by LeetCode, changing my code to fit this by making the 
input linked lists a listNode and iterating it through each value of the inputs. 

Time Complexity:  O(n)
Space Complexity: O(n)

Issues:
The ListNode class isn't functional. Moreover, the output is still a list rather than a linked list.

Tests:
ListNode([2,4,3]), ListNode([5,6,4]) --> time limit exceeded
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

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
            output += firstL1.val*pow(10, n)
            firstL1 = firstL1.next
        for n in range(self.len(l2)):
            output+=firstL2.val*pow(10, n)
            firstL2 = firstL2.next

        output = str(output)
        new = []
        for item in output:
            new.append(int(item))
        new.reverse()

        return new


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
    print(sol.addTwoNumbers(ListNode([2,4,3]), ListNode([5,6,4])))
