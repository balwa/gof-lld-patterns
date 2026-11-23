"""COMMAND - encapsulate a request as an object (queue, log, undo).
Use when: undo/redo, task queues.  Exercise: add redo."""
class Light:
    def __init__(self): self.on = False
class On:
    def __init__(self, l): self.l = l
    def execute(self): self.l.on = True
    def undo(self): self.l.on = False
class Remote:
    def __init__(self): self.history = []
    def press(self, cmd): cmd.execute(); self.history.append(cmd)
    def undo(self): self.history.pop().undo()

def demo():
    l, r = Light(), Remote(); r.press(On(l)); print(l.on); r.undo(); print(l.on)
    assert l.on is False

if __name__ == "__main__": demo()
