"""PROXY - a stand-in that controls access to another object (lazy, cache, auth).
Use when: virtual/protection/caching proxy.  Exercise: add an access-control proxy."""
class RealImage:
    def __init__(self, f): self.f = f; print(f"  loading {f} from disk (slow)")
    def show(self): return f"showing {self.f}"
class ImageProxy:
    def __init__(self, f): self.f, self._real = f, None
    def show(self):
        if self._real is None: self._real = RealImage(self.f)  # lazy
        return self._real.show()

def demo():
    p = ImageProxy("cat.png")   # nothing loaded yet
    print(p.show()); print(p.show())

if __name__ == "__main__": demo()
