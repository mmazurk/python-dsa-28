
from doctest import debug


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} --> {self.next}"

# I originally wanted to generate dynamic names for the nodes, but this is not ever recommended
# Instead, just put them into a dictionaries or lists
# That makes it easy to iterate through and set the self.next values

# I also didn't understand that the __repr__ function will recursively run on {self.next}
# So you end up getting 1 --> 2 --> 3 --> 4 --> 5 when you print the first node
# I didn't realize that by returning just the first node from my list, the other nodes were still alive in memory
# because they are assigned in a chain from the first node to the last
# Lastly, my brain just doesn't understand the order of operations for reversing a linked list
# The order is this:
# start by establishing what is your previous_node and current_node when you are at head
# then in the while loop
# (1) create a variable to remember the next node, (2) set current.next to previous, (3) update previous to current
# and (4) move to the next node
# It seems so simple yet I am absolutely confounded when I try to do it


class Solution():
    def createList(self, items):
        listnodes = []
        for item in items:
            listnodes.append(ListNode(item))

        for i in range(0, len(listnodes)-1):
            listnodes[i].next = listnodes[i+1]

        return listnodes[0]

    def reverseIterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        print(head)

        previous_node = None
        current_node = head

        while (current_node):
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return previous_node

# What you are actually doing in this:
# is digging down with recursive calls until you figure out the new head
# Once you do, that stays CONSTANT
# Then when it unwinds it does the reversing of the arrows on variable = head (not newHead)
# This is what baked your brain
# head.next.next reverses the arrow
# head.next erases the old arrow

    def reverseRecursive(self, head):
        print(head)

        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseRecursive(head.next)
            head.next.next = head
        head.next = None

        return newHead


solution = Solution()
head = solution.createList([1, 2, 3, 4, 5])
reversed_list = solution.reverseRecursive(head)
print(reversed_list)


# Here's my diagram:
# head = 1
# newHead = rR(2)
# 	head = 2
# 	newHead = rR(3)
# 		head = 3
# 		newHead = rR(4)
# 			head =4
# 			newHead = rr(5)

# Now you build the reversed list

# 			head = 4
# 			nH = 5
# 			5.next = 4
# 			4.next = none
# 		head = 3
# 		nH = 5
# 		4.next = 3
# 		3.next = none
# 	head = 2
# 	nH = 5
# 	3.next = 2
# 	2.next = none
# head = 1
# nH = 5
# 2.next = 1
# 1.next = none
