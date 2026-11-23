"""FLYWEIGHT - share common (intrinsic) state to save memory.
Use when: thousands of similar objects (trees in a game, glyphs).  Exercise: measure memory."""
class TreeType:
    def __init__(self, name, texture): self.name, self.texture = name, texture
class TreeFactory:
    _types = {}
    @classmethod
    def get(cls, name, texture):
        return cls._types.setdefault((name, texture), TreeType(name, texture))
class Tree:  # extrinsic state (x, y) lives here
    def __init__(self, x, y, t): self.x, self.y, self.type = x, y, t

def demo():
    forest = [Tree(i, i, TreeFactory.get("oak", "green.png")) for i in range(1000)]
    print(len(forest), "trees,", len(TreeFactory._types), "shared type")
    assert len(TreeFactory._types) == 1

if __name__ == "__main__": demo()
