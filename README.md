# dsa-bonus-assignment-1-text-editor

Data Structures & Algorithms S-2023 | Hertie School | Extra Credit Assignment 1 - Text Editor

@authors: Oskar Krafft | Paul Sharratt | Fabian Metz | Amin Oueslati

## Scope

In this project we develop a simple text editor using a positiona list class. The text editor allows for the following operations:
- left: Move cursor to the left by one character
- right: Move cursor to the right by one character
- insert: Insert a character just after the cursor
- delete: Delete the character just after the cursor

## Content

1. positional_list.py: Creates the PositionalList class, which is a doubly-linked list with sentinel head and tail nodes. 
2. text_editor.py: Contains the TextEditor class, which uses the PositionalList class to store and display a string of characters, along with a cursor object, which allows the user to navigate the string and perform the aforementioned operations. The cursor is depicted by a ^ symbol under the corresponding string.
3. test.py: A test of the text editor showcasing the different functionalities. 