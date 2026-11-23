"""STATE - object behavior changes with its internal state; each state is a class.
Use when: vending machines, order lifecycle, if/elif state ladders.  Exercise: add 'Cancelled'."""
class Ordered:
    def next(self): return Shipped()
    name = "ordered"
class Shipped:
    def next(self): return Delivered()
    name = "shipped"
class Delivered:
    def next(self): return self
    name = "delivered"
class Order:
    def __init__(self): self.state = Ordered()
    def advance(self): self.state = self.state.next()

def demo():
    o = Order()
    for _ in range(3): print(o.state.name); o.advance()
    assert o.state.name == "delivered"

if __name__ == "__main__": demo()
