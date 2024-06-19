
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"


class Solution():
    def createList(self, items, asList):
        listnodes = []
        for item in items:
            listnodes.append(ListNode(item))

        for i in range(0, len(listnodes)-1):
            listnodes[i].next = listnodes[i+1]

        listnodes[1].next = listnodes[1]

        if (asList):
            return listnodes
        else:
            return listnodes[0]

    # My solution didn't work because you check the value of next and there could be repeats in the linked list
    # I also didn't realize that the cycle can only come at the end
    # Nice try, but not good.

    def hasCycleMark(self, head):

        next_values = {}

        currentNode = head
        while (currentNode):
            if (currentNode.next):
                value = currentNode.next.val
                next_values[value] = next_values.get(value, 0) + 1
                if next_values[value] > 1:
                    return True
            currentNode = currentNode.next
        return False

# I didn't realize it when I started this problem, but the cycle can only come at the end
# since every Node object can only have one value for .next

# That said, the trick here is to set up two pointers;
# one that moves one step at a time
# and one that moves two steps at a time
# The slow pointer will eventually catch up to the fast one if there is a cycle at the end. Makes sense, right?
# I mean, I never would have thought of it, m'butokay.

# By the way, this has a name too. It's called "Floyd's Cycle Detection Algorithm"
# I bet Floyd had more than 15 minutes to come up with this and wasn't sweating it out an in interview

    def hasCycle(self, head):

        if not head or head.next == None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


solution = Solution()
listnodes = solution.createList([1, 2, 3, 4, 5, 6, 7], asList=True)
for item in listnodes:
    print(item, "--->", item.next)

head = solution.createList([3, 2, 0, -4], asList=False)
print(solution.hasCycle(head))
