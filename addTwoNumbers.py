# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        array = [self.val]
        nextNode = self.next
        while(nextNode != None):
            array.append(nextNode.val)
            nextNode = nextNode.next
        return str(array)

def generateLinkedList(numArray):
    list_node = ListNode(numArray[0])
    curNode = list_node
    for num in numArray[1:]:
        newNode = ListNode(num)
        curNode.next = newNode
        curNode = curNode.next
    return list_node

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.addTwoNumbersHelper(l1, l2, 0)
    def addTwoNumbersHelper(self, l1, l2, prev_carry_over):
        remainder = (l1.val + l2.val + prev_carry_over) % 10
        curr_carry_over = (l1.val + l2.val + prev_carry_over) >= 10
        l1.val = remainder
        if (l1.next == None and l2.next == None and not curr_carry_over):
            return l1
        if (l1.next == None):
            l1.next = ListNode()
        if (l2.next == None):
            l2.next = ListNode()
        self.addTwoNumbersHelper(l1.next, l2.next, curr_carry_over)
        return l1

if __name__ == "__main__":
    numArray1 = [9,9,9,9,9,9,9]
    numArray2 = [9,9,9,9]
    l1 = generateLinkedList(numArray1)
    l2 = generateLinkedList(numArray2)
    print(l1)
    print(l2)
    solution = Solution()
    print(solution.addTwoNumbers(l1, l2))
