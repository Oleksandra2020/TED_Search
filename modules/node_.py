"""
Initializes Node and TwoWayNode classes for building
linked list data structure
"""


class Node:
    """
    Node representation for building linked lists
    """

    def __init__(self, data=None, next=None):
        """
        str, obj -> None
        Initializes the knot
        """
        self.data = data
        self.next = next

    def head(self):
        """
        obj -> obj
        Returns the head of the linked list
        >>> val = Node()
        >>> val.data, val.next = 4, Node(5, Node(7))
        >>> val.head().data
        4
        """
        return self

    def get_translator(self):
        """
        () -> str
        Returns the translator out of linked list
        """
        return self.data
    
    def get_id(self):
        """
        () -> str
        Returns the video id out of linked list
        """
        return self.next.data

    def get_title(self):
        """
        () -> str
        Returns the title out of linked list
        """
        return self.next.next.data

    def get_tf(self):
        """
        () -> str
        Returns the term frequency out of linked list
        """
        return self.next.next.data

    def get_description(self):
        """
        () -> str
        Returns the desciption of video out of linked list
        """
        return self.tail().data

    def get_views(self):
        """
        () -> str
        Returns the views out of linked list
        """
        return self.next.next.next.data

    def get_ted_link(self):
        """
        () -> str
        Returns the ted link out of linked list
        """
        return self.next.next.next.next.data

    def tail(self):
        """
        obj -> obj
        Returns the tail of the linked list
        >>> val = Node()
        >>> val.data, val.next = 4, Node(5, Node(7))
        >>> val.tail(val).data
        7
        """
        node = self
        while node.next:
            node = node.next
        return node

    def __str__(self):
        """
        () -> str
        Returns the string representation of a linked list to the user
        >>> val = Node()
        >>> val.data, val.next = 4, Node(5, Node(7))
        >>> print(val)
        4 5 7 
        """
        node = self
        s = ''
        while node:
            s += str(node.data) + ' '
            node = node.next
        return s


class TwoWayNode(Node):
    """
    Two way linked list representation
    """

    def __init__(self, data=None, next=None, previous=None):
        """
        str, obj -> None
        Initializes the knot
        """
        self.data = data
        self.next = next
        self.previous = previous

    def __str__(self):
        """
        () -> str
        Returns the string representation of a linked list to the user
        >>> val = Node()
        >>> val.data, val.next = 4, Node(5, Node(7))
        >>> val = val.next
        >>> val.previous = Node(8)
        >>> print(val)
        5 7 
        """
        node = self
        s = ''
        while node:
            s += str(node.data) + ' '
            node = node.next
        return s
