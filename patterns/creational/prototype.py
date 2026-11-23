"""PROTOTYPE - create new objects by cloning an existing one.
Use when: creation is expensive or you need copies of configured objects.
Exercise: shallow vs deep copy - what breaks with copy.copy here?"""
import copy

class Document:
    def __init__(self, title, tags): self.title, self.tags = title, tags
    def clone(self): return copy.deepcopy(self)

def demo():
    tpl = Document("Report", ["draft"])
    d = tpl.clone(); d.tags.append("q3")
    print(tpl.tags, d.tags)
    assert tpl.tags == ["draft"]

if __name__ == "__main__": demo()
