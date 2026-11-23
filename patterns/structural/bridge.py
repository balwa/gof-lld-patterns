"""BRIDGE - split abstraction from implementation so both vary independently.
Use when: avoiding class explosion (shapes x renderers).  Exercise: add a Square."""
class VectorRenderer:
    def circle(self, r): return f"vector circle r={r}"
class RasterRenderer:
    def circle(self, r): return f"pixels circle r={r}"

class Circle:
    def __init__(self, renderer, r): self.renderer, self.r = renderer, r
    def draw(self): return self.renderer.circle(self.r)

def demo():
    for r in (VectorRenderer(), RasterRenderer()): print(Circle(r, 5).draw())
    assert Circle(RasterRenderer(), 2).draw().startswith("pixels")

if __name__ == "__main__": demo()
