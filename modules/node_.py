class Node:
    """
    Linked list representation
    """

    def __init__(self, data=None, next=None):
        """
        str, obj -> None
        Initializes the knot
        """
        self.data = data
        self.next = next

    def tail(self, head):
        """
        obj -> obj
        Returns the tail of the linked list
        """
        node = head
        while node.next:
            node = node.next
        return node

    def __str__(self):
        """
        () -> str
        Returns the string representation of a linked list to the user
        """
        node = self
        s = ''
        while node:
            s += str(node.data) + ' '
            node = node.next
        return s
