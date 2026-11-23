"""VISITOR - add operations to a class hierarchy without modifying it.
Use when: stable shapes, many operations (area, export).  Exercise: add a Perimeter visitor."""
import math
class Circle:
    def __init__(self, r): self.r = r
    def accept(self, v): return v.visit_circle(self)
class Rect:
    def __init__(self, w, h): self.w, self.h = w, h
    def accept(self, v): return v.visit_rect(self)
class Area:
    def visit_circle(self, c): return round(math.pi * c.r ** 2, 2)
    def visit_rect(self, r): return r.w * r.h

def demo():
    print([s.accept(Area()) for s in (Circle(1), Rect(2, 3))])
    assert Rect(2, 3).accept(Area()) == 6

if __name__ == "__main__": demo()
