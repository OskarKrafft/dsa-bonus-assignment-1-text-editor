"""
Submitted on 6th May 2023

bonus assignment 1: text-editor

@authors: Oskar Krafft | Paul Sharratt | Fabian Metz | Amin Oueslati
"""

from positional_list import PositionalList

class TextEditor:
    def __init__(self):
        self.text = PositionalList()
        self.cursor = self.text.tail  # Set initial cursor position to the tail sentinel node

    def left(self):
        """Move the cursor left, unless it's at the beginning"""
        if self.cursor.prev.prev is not None:
            self.cursor = self.cursor.prev

    def right(self):
        """Move the cursor right, unless it's at the end"""
        if self.cursor.next is not self.text.tail:
            self.cursor = self.cursor.next

    def insert(self, c):
        """Insert the character c just before the cursor"""
        self.text.insert_before(self.cursor, c)

    def delete(self):
        """Delete the character at the cursor position, unless it's at the head"""
        if self.cursor.element is not None:
            if self.cursor == self.text.head.next:
                self.text.head.next = self.cursor.next
                self.cursor.next.prev = self.text.head
                self.cursor = self.cursor.next
            elif self.cursor == self.text.tail.prev:
                self.text.tail.prev = self.cursor.prev
                self.cursor.prev.next = self.text.tail
                self.cursor = self.cursor.prev
            else:
                self.cursor.prev.next = self.cursor.next
                self.cursor.next.prev = self.cursor.prev
                self.cursor = self.cursor.next
            self.text.size -= 1

    def display(self):
        """Display the text and underline the cursor position"""
        string = ""
        underline = ""
        current = self.text.head.next
        while current.element is not None:
            string += current.element
            underline += "^" if current.next == self.cursor else " "
            current = current.next
        print(string)
        print(underline)