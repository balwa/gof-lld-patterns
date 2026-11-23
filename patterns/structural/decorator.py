"""DECORATOR - add behavior to an object dynamically by wrapping it.
Use when: optional features combine freely (coffee add-ons).  Exercise: add Whip."""
class Coffee:
    def cost(self): return 50
    def desc(self): return "coffee"
class AddOn:
    def __init__(self, inner): self.inner = inner
class Milk(AddOn):
    def cost(self): return self.inner.cost() + 10
    def desc(self): return self.inner.desc() + " + milk"
class Sugar(AddOn):
    def cost(self): return self.inner.cost() + 5
    def desc(self): return self.inner.desc() + " + sugar"

def demo():
    c = Sugar(Milk(Coffee())); print(c.desc(), c.cost()); assert c.cost() == 65

if __name__ == "__main__": demo()
