"""COMPOSITE - treat single objects and groups uniformly (tree structures).
Use when: file systems, org charts, menus.  Exercise: add a count_files() method."""
class File:
    def __init__(self, name, size): self.name, self.size = name, size
    def total(self): return self.size
class Folder:
    def __init__(self, name, *children): self.name, self.children = name, list(children)
    def total(self): return sum(c.total() for c in self.children)

def demo():
    root = Folder("root", File("a", 10), Folder("sub", File("b", 5), File("c", 7)))
    print(root.total()); assert root.total() == 22

if __name__ == "__main__": demo()
