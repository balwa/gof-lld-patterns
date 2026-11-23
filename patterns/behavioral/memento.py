"""MEMENTO - capture and restore an object's state without breaking encapsulation.
Use when: editor undo, game saves.  Exercise: limit history to 5 snapshots."""
class Editor:
    def __init__(self): self.text = ""
    def save(self): return self.text           # memento
    def restore(self, m): self.text = m

def demo():
    e, history = Editor(), []
    e.text = "hello"; history.append(e.save())
    e.text = "hello world"; e.restore(history.pop())
    print(e.text); assert e.text == "hello"

if __name__ == "__main__": demo()
