"""
Submitted on 6th May 2023

bonus assignment 1: text-editor

@authors: Oskar Krafft | Paul Sharratt | Fabian Metz | Amin Oueslati
"""

class PositionalList:
    """Define Node class to represent elements in the linked list"""
    class Node:
        def __init__(self, element, prev=None, next=None):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        """Initialize the head and tail sentinel nodes"""
        self.head = self.Node(None)
        self.tail = self.Node(None, self.head)
        self.head.next = self.tail
        self.size = 0

    def insert_before(self, node, element):
        """Insert a new node with the specified element before the given node"""
        new_node = self.Node(element, node.prev, node)
        node.prev.next = new_node
        node.prev = new_node
        self.size += 1
        return new_node

    def delete_node(self, node):
        """Remove the given node from the list and return its element"""
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node.element