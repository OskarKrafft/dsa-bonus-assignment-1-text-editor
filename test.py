"""
Submitted on 6th May 2023

bonus assignment 1: text-editor

@authors: Oskar Krafft | Paul Sharratt | Fabian Metz | Amin Oueslati
"""


from text_editor import TextEditor

# Example usage of the TextEditor class
editor = TextEditor()

editor.insert("H")
editor.insert("e")
editor.insert("l")
editor.insert("l")
editor.insert("o")
editor.insert(" ")
editor.insert("G")
editor.insert("o")
editor.insert("n")
editor.insert("d")
editor.insert("a")
editor.insert("l")
editor.insert("f")

editor.left()
editor.left()
editor.left()
editor.left()
editor.left()
editor.left()

editor.display()
editor.delete()
editor.insert("a")

editor.display()
